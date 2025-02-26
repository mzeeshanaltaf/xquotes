def generate_html_template_1(response):

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
                align-items: stretch;
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
                width: 150px; /* Fixed width */
                display: flex;
                align-items: center;
                justify-content: center;
                text-align: center;
                border-radius: 5px 0 0 5px;
                word-wrap: break-word;
                white-space: normal;
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

def generate_html_template_2(response):
    colors = ["#E74C3C", "#F39C12", "#27AE60", "#2980B9", "#8E44AD"]  # Define colors for labels
    html_template = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Summary</title>
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

            .summary-item {{
                display: flex;
                align-items: stretch; /* Make items stretch to equal height */
                background: white;
                margin: 15px 0;
                border-radius: 10px;
                box-shadow: 2px 2px 10px rgba(0, 0, 0, 0.1);
                overflow: hidden; /* Ensures clean alignment */
            }}

            .summary-label {{
                color: white;
                padding: 20px;
                font-weight: bold;
                font-size: 16px;
                min-width: 200px; /* Fixed width */
                max-width: 200px; /* Ensures width remains the same */
                text-align: center;
                border-radius: 5px 0 0 5px;
                text-transform: uppercase;
                display: flex;
                align-items: center;
                justify-content: center;
                word-wrap: break-word; /* Wraps long text properly */
            }}

            .summary-text {{
                padding: 20px;
                font-size: 14px;
                color: #555;
                background: white;
                flex: 1;
                border-radius: 0 5px 5px 0;
            }}

            .summary-text ul {{
                margin: 0;
                padding-left: 20px;
            }}

            .summary-text li {{
                margin-bottom: 5px;
                line-height: 1.6;
            }}
        </style>
    </head>
    <body>

        <div class="container">
    """

    for idx, (category, points) in enumerate(response["bullet_points"].items(), start=1):
        color = colors[(idx - 1) % len(colors)]  # Rotate colors dynamically
        html_template += f"""
            <div class="summary-item">
                <div class="summary-label" style="background: {color};">
                    {category}
                </div>
                <div class="summary-text">
                    <ul>
                        {''.join(f"<li>{point}</li>" for point in points)}
                    </ul>
                </div>
            </div>
        """

    html_template += """
        </div>
    </body>
    </html>
    """

    return html_template

def generate_html_template_3(response):
    colors = ["#D98880", "#5D6D7E", "#85929E", "#AAB7B8", "#D7DBDD"]  # Define colors for labels

    html_template = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Summary</title>
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

            .summary-item {{
                background: white;
                margin: 15px 0;
                border-radius: 5px;
                box-shadow: 2px 2px 10px rgba(0, 0, 0, 0.1);
                overflow: hidden;
            }}

            .summary-header {{
                padding: 10px 15px;
                font-weight: bold;
                font-size: 16px;
                background-color: #BDC3C7;
                color: white;
            }}

            .summary-text {{
                padding: 15px;
                font-size: 14px;
                color: #555;
                background: white;
            }}

            .summary-text ul {{
                margin: 0;
                padding-left: 20px;
            }}

            .summary-text li {{
                margin-bottom: 5px;
                line-height: 1.6;
            }}
        </style>
    </head>
    <body>

        <div class="container">
    """

    for idx, (category, points) in enumerate(response["bullet_points"].items()):
        color = colors[idx % len(colors)]  # Cycle colors dynamically
        html_template += f"""
            <div class="summary-item">
                <div class="summary-header" style="background: {color};">
                    {category}
                </div>
                <div class="summary-text">
                    <ul>
                        {''.join(f"<li>{point}</li>" for point in points)}
                    </ul>
                </div>
            </div>
        """

    html_template += """
        </div>
    </body>
    </html>
    """

    return html_template

def generate_html_template_4(response):
    colors = ["#1F4E79", "#005A87", "#BF9000", "#B03A2E", "#117A65"]  # Colors for category titles

    html_template = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Agenda Summary</title>
        <style>
            @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600&display=swap');

            body {{
                font-family: 'Poppins', sans-serif;
                background-color: #f4f7fc;
                margin: 0;
                padding: 0;
                display: flex;
                justify-content: center;
            }}

            .container {{
                width: 80%;
                margin: 40px 0;
                background: white;
                padding: 20px;
            }}

            .agenda-item {{
                display: flex;
                align-items: flex-start;
                border-bottom: 1px solid #ddd;
                padding: 15px 0;
            }}

            .agenda-number {{
                font-size: 24px;
                font-weight: bold;
                color: #666;
                width: 50px;
                text-align: center;
            }}

            .separator {{
                width: 2px;
                background: #666;
                height: 100%;
                margin: 0 15px;
            }}

            .agenda-content {{
                flex: 1;
            }}

            .agenda-title {{
                font-size: 18px;
                font-weight: bold;
                margin-bottom: 5px;
            }}

            .agenda-text ul {{
                margin: 5px 0;
                padding-left: 18px;
                font-size: 14px;
                color: #444;
            }}

            .agenda-text li {{
                margin-bottom: 5px;
                line-height: 1.5;
            }}
        </style>
    </head>
    <body>
        <div class="container">
    """

    for idx, (category, points) in enumerate(response["bullet_points"].items(), start=1):
        color = colors[idx % len(colors)]  # Cycle through colors
        html_template += f"""
            <div class="agenda-item">
                <div class="agenda-number"> {idx:02} </div>
                <div class="separator"></div>
                <div class="agenda-content">
                    <div class="agenda-title" style="color: {color};">
                        {category}
                    </div>
                    <div class="agenda-text">
                        <ul>
                            {''.join(f"<li>{point}</li>" for point in points)}
                        </ul>
                    </div>
                </div>
            </div>
        """

    html_template += """
        </div>
    </body>
    </html>
    """

    return html_template

def generate_html_template_5(response):
    colors = ["#BF8970", "#3D5A80", "#1F4E79", "#2C3E50"]  # Alternating colors

    html_template = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Summary Points</title>
        <style>
            @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600&display=swap');

            body {{
                font-family: 'Poppins', sans-serif;
                background-color: #f4f7fc;
                margin: 0;
                padding: 0;
                display: flex;
                justify-content: center;
            }}

            .container {{
                width: 80%;
                margin: 40px 0;
                background: white;
                padding: 20px;
            }}

            .summary-item {{
                display: flex;
                align-items: center;
                margin-bottom: 20px;
            }}

            .arrow-box {{
                color: white;
                font-weight: bold;
                font-size: 16px;
                padding: 15px 20px;
                width: 30%;  /* 1/3rd of the space */
                text-align: center;
                position: relative;
                border-radius: 5px;
                flex-shrink: 0;
            }}

            .text-content {{
                background: #F8F9FA;
                padding: 15px;
                margin-left: 20px;  /* Space between arrow and text box */
                border-radius: 5px;
                width: 65%;  /* 2/3rd of the space */
                box-shadow: 2px 2px 8px rgba(0, 0, 0, 0.1);
            }}

            .text-content ul {{
                padding-left: 20px;
                font-size: 14px;
                color: #444;
            }}

            .text-content li {{
                margin-bottom: 5px;
                line-height: 1.5;
            }}
        </style>
    </head>
    <body>
        <div class="container">
    """

    for idx, (category, points) in enumerate(response["bullet_points"].items()):
        color = colors[idx % len(colors)]  # Cycle through colors
        html_template += f"""
            <div class="summary-item">
                <div class="arrow-box" style="background-color: {color}; position: relative;">
                    {category}
                    <div style="
                        content: '';
                        position: absolute;
                        top: 50%;
                        left: 100%;
                        transform: translateY(-50%);
                        border-top: 15px solid transparent;
                        border-bottom: 15px solid transparent;
                        border-left: 20px solid {color}; /* Arrow color matches box */
                    "></div>
                </div>
                <div class="text-content">
                    <ul>
                        {''.join(f"<li>{point}</li>" for point in points)}
                    </ul>
                </div>
            </div>
        """

    html_template += """
        </div>
    </body>
    </html>
    """

    return html_template





