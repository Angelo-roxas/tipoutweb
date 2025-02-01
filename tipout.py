from flask import Flask, request, render_template_string

app = Flask(__name__)

TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Tipout Calculator</title>
    <style>
        body { font-family: Arial, sans-serif; text-align: center; margin: 50px; }
        input { margin: 5px; padding: 8px; }
        button { padding: 10px; cursor: pointer; }
    </style>
</head>
<body>
    <h2>Tipout Calculator</h2>
    <form method="POST">
        <label>Total Sales:</label>
        <input type="number" step="0.01" name="total_sales" required>
        <br><br>
        <label>Net Cash Owed:</label>
        <input type="number" step="0.01" name="net_cash_owed" required>
        <br><br>
        <button type="submit">Calculate</button>
    </form>

    {% if bar_tipout is not none %}
        <h3>Results:</h3>
        <p>Bar Tipout: ${{ bar_tipout }}</p>
        <p>House Tipout: ${{ house_tipout }}</p>
        <p>Total Due: ${{ total_due }}</p>
    {% endif %}
</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def calculate():
    if request.method == "POST":
        try:
            total_sales = float(request.form["total_sales"])
            net_cash_owed = float(request.form["net_cash_owed"])

            bar_tipout = round(total_sales * 0.015, 2)
            house_tipout = round(total_sales * 0.0575, 2)
            total_due = round(net_cash_owed + house_tipout, 2)

            return render_template_string(TEMPLATE, bar_tipout=bar_tipout, house_tipout=house_tipout, total_due=total_due)
        except ValueError:
            return render_template_string(TEMPLATE, error="Invalid input!")

    return render_template_string(TEMPLATE, bar_tipout=None, house_tipout=None, total_due=None)

if __name__ == "__main__":
    app.run(debug=True)
