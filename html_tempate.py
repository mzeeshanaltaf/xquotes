def generate_html_template(response):

    html_template = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>{response['title']}</title>
        <style>
            @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600&display=swap');

            body {{
                font-family: 'Poppins', sans-serif;
                background-color: #f4f7fc;
                margin: 0;
                padding: 0;
            }}

            .container {{
                width: 80%;
                margin: auto;
                padding: 20px;
            }}

            .header {{
                background-color: #1f2937;
                color: white;
                text-align: center;
                padding: 20px;
                font-size: 24px;
                font-weight: bold;
            }}

            .summary-item {{
                display: flex;
                align-items: center;
                background: white;
                margin: 15px 0;
                padding: 15px;
                border-radius: 10px;
                box-shadow: 2px 2px 10px rgba(0, 0, 0, 0.1);
            }}

            .summary-label {{
                background: #2c3e50;
                color: white;
                padding: 15px 20px;
                font-weight: bold;
                font-size: 16px;
                min-width: 150px;
                position: relative;
                text-align: center;
                border-radius: 5px 0 0 5px;
            }}

            .summary-label::after {{
                content: "";
                position: absolute;
                right: -15px;
                top: 50%;
                transform: translateY(-50%);
                border-left: 15px solid #2c3e50;
                border-top: 15px solid transparent;
                border-bottom: 15px solid transparent;
            }}

            .summary-text {{
                padding: 15px;
                font-size: 14px;
                color: #555;
                background: white;
                flex: 1;
                border-radius: 0 5px 5px 0;
            }}
        </style>
    </head>
    <body>

        <div class="header">{response['title']}</div>

        <div class="container">
    """
    for category, points in response["bullet_points"].items():
        html_template += f"""
            <div class="summary-item">
                <div class="summary-label">{category}</div>
                <div class="summary-text">
                    <ul>
        """
        for point in points:
            html_template += f"<li>{point}</li>\n"

        html_template += """</ul>
                </div>
            </div>
        """

    html_template += """
        </div>
    </body>
    </html>
    """
    return html_template