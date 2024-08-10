<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Carbon Footprint Calculator</title>
    <script>
        async function calculateEmissions() {
            const activity = document.getElementById('activity').value;
            const amount = parseFloat(document.getElementById('amount').value);

            const response = await fetch('http://127.0.0.1:5000/calculate', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({ activity, amount })
            });

            const result = await response.json();
            document.getElementById('result').innerText = `Emissions: ${result.emission} kg CO2`;
        }
    </script>
</head>
<body>
    <h1>Carbon Footprint Calculator</h1>
    <label for="activity">Activity:</label>
    <select id="activity">
        <option value="car">Car</option>
        <option value="flight">Flight</option>
        <option value="electricity">Electricity</option>
    </select>
    <br>
    <label for="amount">Amount:</label>
    <input type="number" id="amount" step="0.01">
    <br>
    <button onclick="calculateEmissions()">Calculate</button>
    <p id="result"></p>
</body>
</html>
