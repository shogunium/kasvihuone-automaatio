let chart;

function toggleTheme() {
    document.body.classList.toggle('dark-mode');
}

function loadData(range) {
    fetch(`/data?range=${range}`)
        .then(response => response.json())
        .then(data => {
            const ctx = document.getElementById('tempChart').getContext('2d');
            if (chart) chart.destroy();
chart = new Chart(ctx, {
    type: 'line',
    data: {
        labels: data.labels,
        datasets: [{
            label: 'Lämpötila (°C)',
            data: data.temps,
            borderColor: 'rgba(75, 192, 192, 1)',
            fill: false
        }]
    },
    options: {
        scales: {
            x: {
                grid: {
                    color: 'rgba(200, 200, 200, 0.2)'
                }
            },
            y: {
                grid: {
                    color: 'rgba(200, 200, 200, 0.2)'
                }
            }
        }
    }
});

            document.getElementById('stats').innerHTML = `
                <p>Korkein: ${data.max} °C | Alin: ${data.min} °C | Keskiarvo: ${data.avg} °C</p>
            `;
        });
}

// Ladataan päivän data oletuksena
loadData('day');
