// DOM Elements
const sliders = {
    study_hours: document.getElementById('study_hours'),
    attendance: document.getElementById('attendance'),
    sleep_hours: document.getElementById('sleep_hours'),
    internet_usage: document.getElementById('internet_usage'),
    assignments_completed: document.getElementById('assignments_completed'),
    previous_score: document.getElementById('previous_score')
};

const valueDisplays = {
    study_hours: document.getElementById('val-study_hours'),
    attendance: document.getElementById('val-attendance'),
    sleep_hours: document.getElementById('val-sleep_hours'),
    internet_usage: document.getElementById('val-internet_usage'),
    assignments_completed: document.getElementById('val-assignments_completed'),
    previous_score: document.getElementById('val-previous_score')
};

const scoreText = document.getElementById('score-text');
const scoreCircle = document.getElementById('score-progress-circle');
const scoreGrade = document.getElementById('score-grade');
const scoreInsight = document.getElementById('score-insight');

const placementGauge = document.getElementById('placement-gauge');
const placementProbText = document.getElementById('placement-prob-text');
const placementBadge = document.getElementById('placement-badge');
const placementBadgeText = document.getElementById('placement-badge-text');

const recommendationText = document.getElementById('recommendation-text');

// Chart objects
let whatIfChartInstance = null;
let importanceChartInstance = null;

// Debounce timer
let debounceTimer;

// Model metrics stored locally after fetch
let modelMetrics = null;

// Initialize Dashboard
document.addEventListener('DOMContentLoaded', () => {
    setupSliders();
    fetchMetrics().then(() => {
        triggerPrediction();
    });
});

// Setup Slider Events
function setupSliders() {
    Object.keys(sliders).forEach(key => {
        sliders[key].addEventListener('input', (e) => {
            // Update value display
            let val = e.target.value;
            if (key === 'attendance') {
                valueDisplays[key].innerText = `${val}%`;
            } else if (key === 'study_hours' || key === 'sleep_hours') {
                valueDisplays[key].innerText = `${val} Jam`;
            } else if (key === 'internet_usage') {
                valueDisplays[key].innerText = `Skala ${val}`;
            } else {
                valueDisplays[key].innerText = val;
            }

            // Trigger debounced prediction
            clearTimeout(debounceTimer);
            debounceTimer = setTimeout(() => {
                triggerPrediction();
            }, 180);
        });
    });
}

// Fetch metrics & Feature Importance from backend
async function fetchMetrics() {
    try {
        const response = await fetch('/api/metrics');
        if (response.ok) {
            modelMetrics = await response.json();
            renderImportanceChart(modelMetrics.regression.feature_importances);
        } else {
            console.error('Failed to load metrics');
        }
    } catch (err) {
        console.error('Error fetching metrics:', err);
    }
}

// Perform prediction based on current slider values
async function triggerPrediction() {
    const data = {
        study_hours: parseInt(sliders.study_hours.value),
        attendance: parseInt(sliders.attendance.value),
        sleep_hours: parseInt(sliders.sleep_hours.value),
        internet_usage: parseInt(sliders.internet_usage.value),
        assignments_completed: parseInt(sliders.assignments_completed.value),
        previous_score: parseInt(sliders.previous_score.value)
    };

    try {
        // 1. Get prediction for current values
        const response = await fetch('/api/predict', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(data)
        });

        if (response.ok) {
            const result = await response.json();
            updateResultsUI(result);
            generateAIRecommendations(data, result);
            
            // 2. Perform What-If simulation data generation (Study Hours 1 to 11)
            updateWhatIfSimulation(data);
        }
    } catch (err) {
        console.error('Error during prediction:', err);
    }
}

// Update prediction results in the UI
function updateResultsUI(data) {
    const score = data.predicted_exam_score;
    const prob = data.placement_probability;
    const status = data.placement_status;

    // A. Update Exam Score Circle Progress
    scoreText.innerText = score.toFixed(1);
    
    // Circumference = 2 * PI * r = 2 * 3.1416 * 50 = 314.16
    const circumference = 314.16;
    const offset = circumference - (score / 100) * circumference;
    scoreCircle.style.strokeDashoffset = offset;

    // Set colors & grade text depending on score range
    let scoreColor = '#dc2626'; // Red
    let grade = 'Kurang';
    let insight = 'Perlu perbaikan segera dalam kebiasaan belajar dan absensi.';

    if (score >= 85) {
        scoreColor = '#10b981'; // Green (Emerald)
        grade = 'Sangat Baik (A)';
        insight = 'Pertahankan ritme belajar luar biasa ini untuk kesuksesan akademik!';
    } else if (score >= 70) {
        scoreColor = '#10b981'; // Green / Emerald (since exam score >= 70 yields Placed)
        grade = 'Baik (B)';
        insight = 'Hasil yang solid. Siap bersaing dan lulus ujian dengan baik.';
    } else if (score >= 55) {
        scoreColor = '#fbbf24'; // Yellow (Amber)
        grade = 'Cukup (C)';
        insight = 'Cukup untuk lulus dasar, namun peluang karir/akademik bisa ditingkatkan.';
    }

    scoreCircle.style.stroke = scoreColor;
    scoreGrade.innerText = grade;
    scoreGrade.style.color = scoreColor;
    scoreInsight.innerText = insight;

    // B. Update Placement Gauge
    const probPct = Math.round(prob * 100);
    placementProbText.innerText = `${probPct}%`;
    placementGauge.style.width = `${probPct}%`;

    // Set gauge colors
    if (prob >= 0.75) {
        placementGauge.style.background = 'var(--grad-emerald)';
        placementGauge.style.boxShadow = '0 0 10px rgba(16, 185, 129, 0.4)';
        placementProbText.style.color = '#34d399';
    } else if (prob >= 0.45) {
        placementGauge.style.background = 'var(--grad-amber)';
        placementGauge.style.boxShadow = '0 0 10px rgba(251, 191, 36, 0.4)';
        placementProbText.style.color = '#fbbf24';
    } else {
        placementGauge.style.background = 'var(--grad-danger)';
        placementGauge.style.boxShadow = '0 0 10px rgba(239, 68, 68, 0.4)';
        placementProbText.style.color = '#f87171';
    }

    // C. Update Placement Badge status
    if (status === 'Placed') {
        placementBadge.className = 'badge-status placed';
        placementBadgeText.innerText = 'PLACED';
        placementBadge.querySelector('i').className = 'fa-solid fa-circle-check';
    } else {
        placementBadge.className = 'badge-status not-placed';
        placementBadgeText.innerText = 'NOT PLACED';
        placementBadge.querySelector('i').className = 'fa-solid fa-circle-xmark';
    }
}

// Generate intelligent advice based on input configuration
function generateAIRecommendations(inputs, results) {
    let recommendations = [];

    if (inputs.sleep_hours < 6) {
        recommendations.push({
            icon: 'fa-bed text-gradient-amber',
            text: '<strong>Kurang Tidur:</strong> Siswa tidur < 6 jam. Kurang tidur mengurangi konsentrasi belajar. Upayakan tidur minimal 7-8 jam.'
        });
    }
    
    if (inputs.attendance < 75) {
        recommendations.push({
            icon: 'fa-calendar-times text-gradient-purple',
            text: '<strong>Kehadiran Kritis:</strong> Kehadiran kelas di bawah 75%. Ini adalah faktor risiko terbesar. Prioritaskan kehadiran kelas.'
        });
    }

    if (inputs.study_hours < 4) {
        recommendations.push({
            icon: 'fa-book-open text-gradient-purple',
            text: '<strong>Jam Belajar Minim:</strong> Jam belajar mandiri kurang dari 4 jam/hari. Tingkatkan waktu belajar terstruktur untuk menaikkan skor.'
        });
    }

    if (inputs.assignments_completed < 10) {
        recommendations.push({
            icon: 'fa-tasks text-gradient-amber',
            text: '<strong>Tugas Terbengkalai:</strong> Penyelesaian tugas di bawah 50%. Mengerjakan tugas membantu memetakan materi ujian.'
        });
    }

    if (inputs.internet_usage > 8) {
        recommendations.push({
            icon: 'fa-wifi text-gradient-indigo',
            text: '<strong>Penggunaan Internet Tinggi:</strong> Skala internet yang tinggi berisiko mendistraksi belajar jika tidak dikontrol.'
        });
    }

    if (recommendations.length === 0) {
        recommendations.push({
            icon: 'fa-circle-check text-gradient-emerald',
            text: '<strong>Pola Belajar Unggul!</strong> Semua metrik (belajar, kehadiran, tidur) berada dalam kondisi optimal. Pertahankan performa ini.'
        });
    }

    // Render Recommendations
    recommendationText.innerHTML = recommendations.map(item => `
        <div class="insight-item">
            <i class="fa-solid ${item.icon}"></i>
            <p>${item.text}</p>
        </div>
    `).join('');
}

// Render "What-If" Simulation Line Chart
async function updateWhatIfSimulation(baseData) {
    // Generate simulation data points: study_hours from 1 to 11
    const studyHoursRange = Array.from({ length: 11 }, (_, i) => i + 1);
    
    const simulationRequests = studyHoursRange.map(hours => {
        const simData = { ...baseData, study_hours: hours };
        return fetch('/api/predict', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(simData)
        }).then(res => res.json());
    });

    try {
        const results = await Promise.all(simulationRequests);
        const examScores = results.map(r => r.predicted_exam_score);
        const placementProbs = results.map(r => r.placement_probability * 100);

        const activeStudyHours = baseData.study_hours;

        if (whatIfChartInstance) {
            // Update existing chart
            whatIfChartInstance.data.datasets[0].data = examScores;
            
            // Highlight current selection with a custom point border width or radius
            const pointRadiusArray = studyHoursRange.map(h => h === activeStudyHours ? 8 : 4);
            const pointBgColorArray = studyHoursRange.map(h => h === activeStudyHours ? '#a78bfa' : '#60a5fa');
            whatIfChartInstance.data.datasets[0].pointRadius = pointRadiusArray;
            whatIfChartInstance.data.datasets[0].pointBackgroundColor = pointBgColorArray;
            
            whatIfChartInstance.update();
        } else {
            // Create Chart
            const ctx = document.getElementById('whatIfChart').getContext('2d');
            const pointRadiusArray = studyHoursRange.map(h => h === activeStudyHours ? 8 : 4);
            const pointBgColorArray = studyHoursRange.map(h => h === activeStudyHours ? '#a78bfa' : '#60a5fa');

            whatIfChartInstance = new Chart(ctx, {
                type: 'line',
                data: {
                    labels: studyHoursRange.map(h => `${h} Jam`),
                    datasets: [{
                        label: 'Prediksi Nilai Ujian',
                        data: examScores,
                        borderColor: '#60a5fa',
                        borderWidth: 3,
                        pointRadius: pointRadiusArray,
                        pointBackgroundColor: pointBgColorArray,
                        pointBorderColor: '#ffffff',
                        tension: 0.35,
                        fill: false
                    }]
                },
                options: {
                    responsive: true,
                    maintainAspectRatio: false,
                    plugins: {
                        legend: { display: false }
                    },
                    scales: {
                        x: {
                            grid: { color: 'rgba(255, 255, 255, 0.05)' },
                            ticks: { color: 'rgba(255, 255, 255, 0.6)' }
                        },
                        y: {
                            min: 20,
                            max: 100,
                            grid: { color: 'rgba(255, 255, 255, 0.05)' },
                            ticks: { color: 'rgba(255, 255, 255, 0.6)' }
                        }
                    }
                }
            });
        }
    } catch (err) {
        console.error('Error simulating What-If:', err);
    }
}

// Render horizontal Feature Importance Bar Chart
function renderImportanceChart(importanceData) {
    const featuresMap = {
        study_hours: 'Jam Belajar',
        attendance: 'Persentase Kehadiran',
        sleep_hours: 'Durasi Tidur',
        internet_usage: 'Penggunaan Internet',
        assignments_completed: 'Tugas Diselesaikan',
        previous_score: 'Skor Ujian Sebelumnya'
    };

    const labels = Object.keys(importanceData).map(k => featuresMap[k] || k);
    const dataValues = Object.values(importanceData).map(v => v * 100); // convert to percentage

    // Sort features descending
    const zipped = labels.map((l, i) => ({ label: l, val: dataValues[i] }));
    zipped.sort((a, b) => b.val - a.val);

    const ctx = document.getElementById('importanceChart').getContext('2d');
    
    importanceChartInstance = new Chart(ctx, {
        type: 'bar',
        data: {
            labels: zipped.map(z => z.label),
            datasets: [{
                data: zipped.map(z => z.val),
                backgroundColor: 'rgba(167, 139, 250, 0.75)',
                borderColor: '#a78bfa',
                borderWidth: 1.5,
                borderRadius: 8,
                barThickness: 16
            }]
        },
        options: {
            indexAxis: 'y', // horizontal bar chart
            responsive: true,
            maintainAspectRatio: false,
            plugins: {
                legend: { display: false }
            },
            scales: {
                x: {
                    max: 40,
                    grid: { color: 'rgba(255, 255, 255, 0.05)' },
                    ticks: { 
                        color: 'rgba(255, 255, 255, 0.6)',
                        callback: function(value) { return value + '%'; }
                    }
                },
                y: {
                    grid: { display: false },
                    ticks: { color: 'rgba(255, 255, 255, 0.8)' }
                }
            }
        }
    });
}
