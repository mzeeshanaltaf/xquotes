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
                overflow: hidden; /* Prevents scrolling */
                display: flex;
                flex-direction: column;
                align-items: center;
                justify-content: center;
                height: 100vh; /* Ensure everything fits within viewport */
            }}

            .container {{
                width: 80%;
                padding: 15px;
                max-height: 85vh; /* Keep within single page */
                overflow: hidden;
                display: flex;
                flex-direction: column;
                justify-content: space-between;
            }}

            .header {{
                background-color: #1f2937;
                color: white;
                text-align: center;
                padding: 15px;
                font-size: 20px;
                font-weight: bold;
            }}

            .summary-item {{
                display: flex;
                align-items: stretch;
                background: white;
                margin: 10px 0;
                padding: 10px;
                border-radius: 8px;
                box-shadow: 2px 2px 8px rgba(0, 0, 0, 0.1);
                flex-wrap: wrap;
            }}

            .summary-label {{
                background: #2c3e50;
                color: white;
                padding: 10px;
                font-weight: bold;
                font-size: 14px;
                width: 120px;
                display: flex;
                align-items: center;
                justify-content: center;
                text-align: center;
                border-radius: 5px 0 0 5px;
                word-wrap: break-word;
                white-space: normal;
            }}

            .summary-text {{
                padding: 10px;
                font-size: 14px;
                color: #555;
                background: white;
                flex: 1;
                border-radius: 0 5px 5px 0;
            }}

            .summary-text ul {{
                padding-left: 15px;
                list-style-type: disc;
                text-align: left;
                margin: 0;
            }}

            .summary-text li {{
                text-align: left;
                margin-bottom: 5px;
                display: list-item;
            }}
        </style>
    </head>
    <body>

        <div class="header">{response['title']}</div>

        <div class="container" id="content">
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

        <script>
            function adjustContent() {
                var container = document.getElementById("content");
                var maxHeight = window.innerHeight * 0.85; // Keep within viewport
                var elements = document.querySelectorAll('.summary-text, .summary-label');
                var fontSize = 16; // Starting font size
                var paddingSize = 10; // Starting padding size

                while (container.scrollHeight > maxHeight && fontSize > 10) {
                    fontSize -= 1;
                    paddingSize -= 1;
                    elements.forEach(el => {
                        el.style.fontSize = fontSize + "px";
                        el.style.padding = paddingSize + "px";
                    });
                }
            }

            window.onload = adjustContent;
            window.onresize = adjustContent;
        </script>

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
                display: flex;
                flex-direction: column;
                align-items: center;
                justify-content: center;
                height: 100vh; /* Full height */
                overflow: hidden; /* Prevent scrolling */
            }}

            .container {{
                width: 80%;
                max-height: 90vh;
                overflow: hidden;
                display: flex;
                flex-direction: column;
                justify-content: space-between;
            }}

            .summary-item {{
                display: flex;
                align-items: stretch;
                background: white;
                margin: 8px 0;
                border-radius: 10px;
                box-shadow: 2px 2px 10px rgba(0, 0, 0, 0.1);
                overflow: hidden;
            }}

            .summary-label {{
                color: white;
                padding: 12px;
                font-weight: bold;
                font-size: 14px;
                min-width: 180px;
                max-width: 180px;
                text-align: center;
                border-radius: 5px 0 0 5px;
                text-transform: uppercase;
                display: flex;
                align-items: center;
                justify-content: center;
                word-wrap: break-word;
            }}

            .summary-text {{
                padding: 12px;
                font-size: 12px;
                color: #555;
                background: white;
                flex: 1;
                border-radius: 0 5px 5px 0;
            }}

            .summary-text ul {{
                margin: 0;
                padding-left: 15px;
            }}

            .summary-text li {{
                margin-bottom: 3px;
                line-height: 1.4;
            }}

        </style>
    </head>
    <body>

        <div class="container" id="content">
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

        <script>
            function adjustContent() {
                var container = document.getElementById("content");
                var maxHeight = window.innerHeight * 0.85;
                var elements = document.querySelectorAll('.summary-text, .summary-label');
                var fontSize = 14;
                var paddingSize = 12;
                var marginSize = 8;
                var lineHeight = 1.4;

                while (container.scrollHeight > maxHeight && fontSize > 10) {
                    fontSize -= 1;
                    paddingSize -= 1;
                    marginSize -= 1;
                    lineHeight -= 0.1;

                    elements.forEach(el => {
                        el.style.fontSize = fontSize + "px";
                        el.style.padding = paddingSize + "px";
                        el.style.margin = marginSize + "px 0";
                        el.style.lineHeight = lineHeight;
                    });
                }
            }

            window.onload = adjustContent;
            window.onresize = adjustContent;
        </script>

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
                display: flex;
                align-items: center;
                justify-content: center;
                min-height: 100vh;
                overflow: hidden; /* Prevents scrolling */
            }}

            .container {{
                width: 80%;
                max-height: 90vh;
                overflow: hidden;
                padding: 20px;
            }}

            .summary-item {{
                background: white;
                margin: 12px 0;
                border-radius: 5px;
                box-shadow: 2px 2px 10px rgba(0, 0, 0, 0.1);
                overflow: hidden;
            }}

            .summary-header {{
                padding: 10px;
                font-weight: bold;
                font-size: 16px;
                background-color: #BDC3C7;
                color: white;
            }}

            .summary-text {{
                padding: 10px;
                font-size: 14px;
                color: #555;
                background: white;
            }}

            .summary-text ul {{
                margin: 0;
                padding-left: 15px;
            }}

            .summary-text li {{
                margin-bottom: 5px;
                line-height: 1.5;
            }}
        </style>
    </head>
    <body>

        <div class="container" id="content">
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

        <script>
            function adjustContent() {
                var container = document.getElementById("content");
                var maxHeight = window.innerHeight * 0.9;
                var elements = document.querySelectorAll('.summary-text, .summary-header');
                var fontSize = 16;
                var paddingSize = 10;
                var marginSize = 12;
                var lineHeight = 1.5;

                while (container.scrollHeight > maxHeight && fontSize > 10) {
                    fontSize -= 1;
                    paddingSize -= 1;
                    marginSize -= 1;
                    lineHeight -= 0.1;

                    elements.forEach(el => {
                        el.style.fontSize = fontSize + "px";
                        el.style.padding = paddingSize + "px";
                        el.style.margin = marginSize + "px 0";
                        el.style.lineHeight = lineHeight;
                    });
                }
            }

            window.onload = adjustContent;
            window.onresize = adjustContent;
        </script>

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
                overflow: hidden;
            }}

            .container {{
                width: 80%;
                margin: 40px 0;
                background: white;
                padding: 20px;
                max-height: 90vh;
                overflow: hidden;
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
        <div class="container" id="content">
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

        <script>
            function adjustContent() {
                var container = document.getElementById("content");
                var maxHeight = window.innerHeight * 0.9;
                var elements = document.querySelectorAll('.agenda-text ul, .agenda-title, .agenda-number');
                var fontSize = 18;
                var paddingSize = 15;
                var lineHeight = 1.5;

                while (container.scrollHeight > maxHeight && fontSize > 10) {
                    fontSize -= 1;
                    paddingSize -= 1;
                    lineHeight -= 0.1;

                    elements.forEach(el => {
                        el.style.fontSize = fontSize + "px";
                        el.style.padding = paddingSize + "px";
                        el.style.lineHeight = lineHeight;
                    });
                }
            }

            window.onload = adjustContent;
            window.onresize = adjustContent;
        </script>
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
                align-items: center;
                height: 100vh;
                overflow: hidden;
            }}

            .container {{
                width: 90%;
                max-height: 95vh;
                background: white;
                padding: 10px;
                box-sizing: border-box;
                overflow: hidden;
                display: flex;
                flex-direction: column;
            }}

            .summary-item {{
                display: flex;
                align-items: center;
                margin-bottom: 10px;
                font-size: 14px; /* Default font size */
            }}

            .arrow-box {{
                color: white;
                font-weight: bold;
                font-size: 14px;
                padding: 10px 15px;
                width: 25%;
                text-align: center;
                border-radius: 5px;
                flex-shrink: 0;
            }}

            .text-content {{
                background: #F8F9FA;
                padding: 10px;
                margin-left: 10px;
                border-radius: 5px;
                width: 70%;
                box-shadow: 1px 1px 4px rgba(0, 0, 0, 0.1);
                font-size: 14px;
                line-height: 1.3;
            }}

            .text-content ul {{
                padding-left: 20px;
                list-style-type: disc !important;
                list-style-position: outside;
                text-align: left;
            }}

            .text-content li {{
                text-align: left;
                display: list-item !important;
            }}
        </style>
    </head>
    <body>
        <div class="container" id="content">
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
                        border-top: 10px solid transparent;
                        border-bottom: 10px solid transparent;
                        border-left: 15px solid {color};
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

        <script>
            function adjustFontSize() {
                var container = document.getElementById("content");
                var maxHeight = window.innerHeight * 0.95; // 95% of viewport height
                var currentFontSize = 14; // Initial font size

                while (container.scrollHeight > maxHeight && currentFontSize > 10) {
                    currentFontSize -= 1; // Reduce font size
                    document.querySelectorAll('.summary-item, .text-content').forEach(el => {
                        el.style.fontSize = currentFontSize + "px";
                    });
                }
            }

            window.onload = adjustFontSize;
            window.onresize = adjustFontSize;
        </script>

    </body>
    </html>
    """

    return html_template






