const ctx = document.getElementById('flowChart').getContext('2d');
const flowChart = new Chart(ctx, {
    type: 'line',
    data: {
        labels: ['10분', '20분', '30분'],
        datasets: [{
            label: '몰입도 변화',
            data: [3, 7, 8],
            borderColor: 'blue',
            fill: false
        }]
    }
});
