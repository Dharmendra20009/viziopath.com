from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/courses')
def courses():
    # Example static course list
    course_list = [
         {"title": "Digital Marketing", "description": "Learn SEO, SEM, content creation, social media management, email marketing, analytics, paid ads, design tools, e-commerce marketing, and communication."},
        {"title": "Banking and Finance", "description": " financial analysis, accounting, risk management, investment planning, banking operations, fintech, regulatory compliance, customer service, and data analysis."},
        {"title": "Business analytics", "description": " data analysis, statistical modeling, data visualization, SQL, Excel, Python/R, predictive analytics, business intelligence tools, and problem-solving."},
        {"title": "Graphic Design", "description": " creativity, typography, color theory, layout design, branding, Adobe Creative Suite (Photoshop, Illustrator, InDesign), UI/UX basics, and visual communication."},
        {"title": "Entrepreneurship", "description": " innovation, leadership, business planning, financial management, risk-taking, problem-solving, networking, marketing, and decision-making."}
    ]
    return render_template('courses.html', courses=course_list)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        # Here you can handle form submission if needed
        pass
    return render_template('contact.html')

@app.route('/mock-test')
def mock_test():
    return render_template('Mock Test.html')

if __name__ == '__main__':
    app.run(debug=True)