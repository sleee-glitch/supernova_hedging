<script src="https://cdn.jsdelivr.net/npm/chartjs-plugin-datalabels@2.0.0"></script>
<script>
Chart.register(ChartDataLabels);
console.log("Script started");

// Common options for bar charts
var commonBarOptions = {
    responsive: true,
    maintainAspectRatio: false,
    plugins: {
        legend: { display: false },
        datalabels: {
            color: '#000',
            anchor: 'end',
            align: 'top',
            formatter: function(value) {
                return value.toFixed(2);
            }
        }
    },
    scales: {
        y: {
            beginAtZero: true
        }
    }
};

// Function to create a chart
function createChart(elementId, type, data, options) {
    var element = document.getElementById(elementId);
    if (!element) {
        console.error(`Element ${elementId} does not exist`);
        return null;
    }

    return new Chart(element.getContext('2d'), {
        type: type,
        data: data,
        options: options
    });
}

// Create charts
var l1_chart = createChart('l1_graph', 'bar', {
    labels: ['p', '1-p'],
    datasets: [{
        data: [{{ x1_l }}, {{ x1_h }}],
        backgroundColor: ['#4682B4', '#D2691E']
    }]
}, {
    ...commonBarOptions,
    plugins: {
        ...commonBarOptions.plugins,
        title: {
            display: true,
            text: 'Lotería 1'
        }
    }
});

var l2_chart = createChart('l2_graph', 'bar', {
    labels: ['p', '1-p'],
    datasets: [{
        data: [{{ x2_h }}, {{ x2_l }}],
        backgroundColor: ['#4682B4', '#D2691E']
    }]
}, {
    ...commonBarOptions,
    plugins: {
        ...commonBarOptions.plugins,
        title: {
            display: true,
            text: 'Lotería 2'
        }
    }
});

var pie_chart = createChart('probability_pie', 'pie', {
    labels: ['p', '1-p'],
    datasets: [{
        data: [{{ p }}, {{ one_minus_p }}],
        backgroundColor: ['#4682B4', '#D2691E']
    }]
}, {
    responsive: true,
    plugins: {
        legend: { position: 'top' },
        title: {
            display: true,
            text: 'Distribución de Probabilidad'
        },
        datalabels: {
            color: '#fff',
            formatter: function(value) {
                return value.toFixed(2);
            }
        }
    }
});

var ev_chart = createChart('ev_graphs', 'bar', {
    labels: ['p', '1-p'],
    datasets: [{
        data: [0, 0],
        backgroundColor: ['#4682B4', '#D2691E']
    }]
}, {
    ...commonBarOptions,
    plugins: {
        ...commonBarOptions.plugins,
        title: {
            display: true,
            text: 'Valores Esperados'
        }
    }
});

function updateEVGraphs(alpha) {
    var ev_down = alpha * {{ x1_l }} + (1 - alpha) * {{ x2_h }};
    var ev_up = alpha * {{ x1_h }} + (1 - alpha) * {{ x2_l }};
    ev_chart.data.datasets[0].data = [ev_down, ev_up];
    ev_chart.update();
}

// Initialize EV graph
updateEVGraphs(0.5);

console.log("Script completed");
</script>