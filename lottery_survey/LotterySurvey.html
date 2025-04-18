{% extends "global/Page.html" %}
{% load otree static %}

{% block title %}
    Round {{ round_number }} of {{ num_rounds }}
{% endblock %}

{% block content %}
<div class="container">
    <div class="row justify-content-center mb-4">
        <div class="col-md-12">
            <ul>         <p> Use the slider to choose how much to allocate to <strong>Investment 1</strong>; the rest will automatically go to <strong>Investment 2</strong>.</p>
        <ul>
            <li> <strong> Possibility A</strong> occurs <strong>{{ p }} </strong> out of <strong>100</strong> cases: <strong> Investment 1  </strong> yields ${{ x1_l }}, while <strong> Investment 2</strong> yields ${{ x2_h }}.</li>
                <li> <strong>Possibility B</strong> occurs <strong>{{ one_minus_p }}</strong> out of <strong>100 </strong> cases: <strong> Investment 1 </strong> yields ${{ x1_h }}, while <strong> Investment 2 </strong> yields ${{ x2_l }}.</li>
            </ul>
        </div>
    </div>
<div style="border: 2px solid black; padding: 10px; margin-top: 10px; border-radius: 5px;">

<div class="container">
  <div class="row justify-content-center">
    <div class="col-md-3">
      <div style="height: 250px; width: 100%;">


        <canvas id="l1_graph"></canvas>
      </div>
    </div>
    <div class="col-md-5">

 <div class="d-flex flex-column justify-content-center mt-4">
<label for="alpha_slider" style="font-size: 0.9em;"> <strong>Select the amount to allocate to Investment 1.</strong>  </label>
<input type="range" min="0.0" max="1" step="0.01" id="alpha_slider" oninput="updateAlphaFromSlider(this.value)" style="width: 100%;">  <div class="d-flex justify-content-between mt-2" style="font-size: 0.7em;">
   <span>$1</span>
    <span>$0.8</span>
    <span>$0.6</span>
    <span>$0.4</span>
    <span>$0.2</span>
    <span>$0.0</span>
  </div>

       <div class="mt-3">
                    <label for="alpha_input"> Confirm your investment ($):</label>
    <input type="number" id="alpha_input" min="0.0" max="1" step="0.01" oninput="validateAlpha()">
  </div>
  <div id="error_message" class="text-danger mt-2" style="display: none;"></div>
  <input type="hidden" name="alpha" id="id_alpha">
</div>

    </div>
    <div class="col-md-3">
      <div style="height: 250px; width: 100%;">
        <canvas id="l2_graph"></canvas>
      </div>
    </div>
  </div>
</div>
<style>

  input[type=range].no-default::-webkit-slider-thumb {
    visibility: hidden;
  }
  input[type=range].no-default::-moz-range-thumb {
    visibility: hidden;
  }
  input[type=range].no-default::-ms-thumb {
    visibility: hidden;
  }

  input[type=range].no-default::-webkit-slider-runnable-track {
    background: lightgray;
  }

  input[type=range].active::-webkit-slider-thumb,
  input[type=range].active::-moz-range-thumb,
  input[type=range].active::-ms-thumb {
    visibility: visible;
  }

  canvas {
    max-width: 100%;
    height: auto !important;
  }
</style>


    <div class="row justify-content-center mt-4">
      <div class="col-md-5">
        <div style="height: 250px; width: 100%;">
          <canvas id="probability_pie"></canvas>
        </div>
      </div>
      <div class="col-md-5">
        <div style="height: 250px; width: 100%;">
          <canvas id="ev_graphs"></canvas>
        </div>
      </div>
    </div>
</div>


<div class="row justify-content-left mt-4">
    <div class="col-md-12 text-left">
        <p> Note, this task can be chosen as the <strong> Round-That-Counts</strong>. </p>
        {% next_button %}
    </div>
</div>

</div>
{% endblock %}
{% block scripts %}
<script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
<script src="https://cdn.jsdelivr.net/npm/chartjs-plugin-datalabels@2.0.0"></script>
<script>
    Chart.register(ChartDataLabels);
    var softBlue = '#4682B4';
    var mutedOrange = '#D2691E';


function updateAlphaFromSlider(value) {
    var reversedValue = (1.01 - parseFloat(value)).toFixed(2);
    var roundedValue = Math.max(0.0, Math.min(1, parseFloat(reversedValue)));
    document.getElementById('alpha_slider').value = value; // Keep original value for slider??
    document.getElementById('id_alpha').value = roundedValue;
    document.getElementById('alpha_input').value = roundedValue;
    updateEVGraphs(roundedValue);
    validateAlpha();
}

function validateAlpha() {
    var sliderValue = parseFloat(document.getElementById('alpha_slider').value);
    var reversedSliderValue = (1.01 - sliderValue).toFixed(2);
    var inputValue = parseFloat(document.getElementById('alpha_input').value || 0);
    var errorMessage = document.getElementById('error_message');
    var nextButton = document.querySelector('.otree-btn-next');

    if (isNaN(inputValue) || inputValue < 0.01 || inputValue > 1) {
        showError("");
        nextButton.disabled = true;
        return false;
    } else if (Math.abs(reversedSliderValue - inputValue) > 0.001) {
        showError("The slider value and input value must match.");
        nextButton.disabled = true;
        return false;
    } else {
        errorMessage.style.display = 'none';
        document.getElementById('id_alpha').value = inputValue.toFixed(2);
        nextButton.disabled = false;
        return true;
    }
}


    var alphaSlider = document.getElementById('alpha_slider');
    var alphaInput = document.getElementById('alpha_input');
var hiddenAlphaInput = document.getElementById('id_alpha');
alphaSlider.value = '';
alphaSlider.classList.add("no-default");

alphaSlider.addEventListener('input', function () {
    alphaSlider.classList.remove("no-default");
    alphaSlider.classList.add("active");
});

alphaInput.value = '';
hiddenAlphaInput.value = '';
hiddenAlphaInput.style.display = 'none';
document.addEventListener("DOMContentLoaded", function() {
    var alphaSlider = document.getElementById('alpha_slider');
    var alphaInput = document.getElementById('alpha_input');
    var hiddenAlphaInput = document.getElementById('id_alpha');
    var nextButton = document.querySelector('.otree-btn-next');
    var errorMessage = document.getElementById('error_message'); // Assuming an error message element

    // Ensure initial state is empty
    alphaSlider.value = "";
    alphaInput.value = "";
    hiddenAlphaInput.value = "";
    nextButton.disabled = true;

    function updateAlphaFromSlider(value) {
        if (value === "") {
            hiddenAlphaInput.value = "";
            alphaInput.value = "";
            nextButton.disabled = true;
            return;
        }
        var reversedValue = (1.01 - parseFloat(value)).toFixed(2);
        var roundedValue = Math.max(0.0, Math.min(1, parseFloat(reversedValue)));
        alphaSlider.value = value;
        hiddenAlphaInput.value = roundedValue;
        alphaInput.value = roundedValue;
        validateAlpha();
    }

    function validateAlpha() {
        var inputValue = alphaInput.value ? parseFloat(alphaInput.value) : NaN;

        if (isNaN(inputValue) || inputValue < 0.01 || inputValue > 1) {
            showError("Please select a valid value.");
            return false;
        } else {
            errorMessage.style.display = "none";
            nextButton.disabled = false;
            return true;
        }
    }

    function showError(message) {
        errorMessage.textContent = message;
        errorMessage.style.display = "block";
        nextButton.disabled = true;
    }

    alphaSlider.addEventListener('input', function() {
        if (this.value === "") {
            alphaInput.value = "";
            hiddenAlphaInput.value = "";
            nextButton.disabled = true;
        } else {
            updateAlphaFromSlider(this.value);
        }
    });

    alphaInput.addEventListener('input', function() {
        var value = parseFloat(this.value);
        if (!isNaN(value) && value >= 0.01 && value <= 1) {
            alphaSlider.value = (1.01 - value).toFixed(2);
            updateAlphaFromSlider(alphaSlider.value);
        } else if (this.value === "") {
            alphaSlider.value = "";
            hiddenAlphaInput.value = "";
            nextButton.disabled = true;
        }
        validateAlpha();
    });

    // Ensure hidden input is not visible
    hiddenAlphaInput.style.display = 'none';
});


    function createChart(ctx, type, data, options) {
    return new Chart(ctx, {
        type: type,
        data: data,
        options: Object.assign({
            responsive: true,
            maintainAspectRatio: false,
            plugins: {
                legend: { display: false },
                datalabels: {
                    color: '#000',
                    font: {
                        weight: 'bold'
                    },
                    formatter: function(value, context) {
                        // For non-percentage values, keep decimal precision
                        return parseFloat(value).toFixed(2);
                    }
                }
            },
            scales: {
                x: {
                    ticks: {
                        callback: function(value, index) {
                            return index === 0 ? '{{ p }}%' : '{{ one_minus_p }}%';
                        }
                    }
                }
            }
        }, options)
    });
}

    var minValue = Math.min({{ x1_l }}, {{ x1_h }}, {{ x2_l }}, {{ x2_h }});
    var maxValue = Math.max({{ x1_l }}, {{ x1_h }}+2, {{ x2_l }}, {{ x2_h }}+2);

    var l1_chart = createChart(document.getElementById('l1_graph').getContext('2d'), 'bar', {
        labels: ['Possibility A', 'Possibility B'],
        datasets: [{
            data: [{{ x1_l }}, {{ x1_h }}],
            backgroundColor: [softBlue, mutedOrange],
            barPercentage: 0.5,
            categoryPercentage: 1.0
        }]
    }, {
        plugins: {
            title: { display: true, text: 'Investment 1' },
            legend: { display: false, position: 'bottom' },
            datalabels: {
                anchor: 'end',
                align: 'top',
            }
        },
        scales: {
            y: { min: minValue, max: maxValue }
        }
    });

    var l2_chart = createChart(document.getElementById('l2_graph').getContext('2d'), 'bar', {
        labels: ['Possibility A', 'Possibility B'],
        datasets: [{
            data: [{{ x2_h }}, {{ x2_l }}],
            backgroundColor: [softBlue, mutedOrange],
            barPercentage: 0.5,
            categoryPercentage: 1.0
        }]
    }, {
        plugins: {
            title: { display: true, text: 'Investment 2' },
            legend: { display: false, position: 'bottom' },
            datalabels: {
                anchor: 'end',
                align: 'top',
            }
        },
        scales: {
            y: { min: minValue, max: maxValue }
        }
    });

var pie_chart = createChart(document.getElementById('probability_pie').getContext('2d'), 'pie', {
    labels: [ 'Possibility B', 'Possibility A'],
    datasets: [{
        data: [{{ one_minus_p }}, {{ p }}],
        backgroundColor: [mutedOrange, softBlue],
        borderWidth: 0
    }]
}, {
    plugins: {
        title: { display: true, text: 'Likelihood of Possibilities' },
        legend: { display: false, position: 'bottom' },
        datalabels: {
            color: '#fff',
            font: {
                weight: 'bold'
            },
            formatter: function(value, context) {
                // Use Math.round() for percentages to avoid decimals
                return context.chart.data.labels[context.dataIndex] + ': ' + Math.round(value);
            }
        }
    }
});
    var ev_chart = createChart(document.getElementById('ev_graphs').getContext('2d'), 'bar', {
        labels: ['Possibility A', 'Possibility B'],
        datasets: [{
            data: [0, 0],
            backgroundColor: [softBlue, mutedOrange],
            barPercentage: 0.5,
            categoryPercentage: 1.0
        }]
    }, {
        plugins: {
            title: { display: true, text: 'Potential Outcome Based on Your Choice' },
            legend: { display: false, text: 'Potential Outcome Based on Your Choice' },
            datalabels: {
                anchor: 'end',
                align: 'top',
            }
        },
        scales: {
            y: { min: minValue, max: maxValue+1 }
        }
    });

function updateEVGraphs(alpha) {
    if (alpha === null) {
        ev_chart.data.datasets[0].data = [0, 0];
    } else {
        var ev_down = (alpha * {{ x1_l }} + (1 - alpha) * {{ x2_h }}).toFixed(2);
        var ev_up = (alpha * {{ x1_h }} + (1 - alpha) * {{ x2_l }}).toFixed(2);
        ev_chart.data.datasets[0].data = [parseFloat(ev_down), parseFloat(ev_up)];
    }
    ev_chart.update();
}


    updateEVGraphs(null);

    alphaSlider.addEventListener('input', function() {
        updateAlphaFromSlider(this.value);
        validateAlpha();
    });

    alphaInput.addEventListener('input', function() {
        validateAlpha();
    });

    // Form submission handler
    document.querySelector('form').addEventListener('submit', function(event) {
        if (!validateAlpha()) {
            event.preventDefault();
            showError("Please choose a number between 0.0 and 1 before submitting.");
        }
    });
    validateAlpha();


</script>
{% endblock %}