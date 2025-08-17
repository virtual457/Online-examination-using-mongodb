<!-- Improved compatibility of back to top link: See: https://github.com/dhmnr/skipr/pull/73 -->
<a id="readme-top"></a>

<!-- *** Thanks for checking out the Best-README-Template. If you have a suggestion *** that would make this better, please fork the repo and create a pull request *** or simply open an issue with the tag "enhancement". *** Don't forget to give the project a star! *** Thanks again! Now go create something AMAZING! :D -->

<!-- PROJECT SHIELDS -->
<!-- *** I'm using markdown "reference style" links for readability. *** Reference links are enclosed in brackets [ ] instead of parentheses ( ). *** See the bottom of this document for the declaration of the reference variables *** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use. *** https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]
<!-- [![LinkedIn][linkedin-shield]][linkedin-url] -->

<!-- PROJECT LOGO -->
<br />
<div align="center">
  <h3 align="center">📚 Online Examination System</h3>

  <p align="center">
    A modern, web-based examination platform built with Flask and MongoDB that enables teachers to create and administer online tests while providing students with a seamless testing experience.
    <br />
    <a href="https://github.com/virtual457/Online-examination-using-mongodb"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/virtual457/Online-examination-using-mongodb">View Demo</a>
    ·
    <a href="https://github.com/virtual457/Online-examination-using-mongodb/issues/new?labels=bug&template=bug-report---.md">Report Bug</a>
    ·
    <a href="https://github.com/virtual457/Online-examination-using-mongodb/issues/new?labels=enhancement&template=feature-request---.md">Request Feature</a>
  </p>
</div>

<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>

<!-- ABOUT THE PROJECT -->
## About The Project

A modern, web-based examination platform built with Flask and MongoDB that enables teachers to create and administer online tests while providing students with a seamless testing experience.

### Key Features

#### For Teachers
- **Secure Login System** - Protected teacher dashboard with session management
- **Question Management** - Add multiple-choice questions with 4 options
- **Bulk Operations** - Delete all questions with one click
- **Real-time Statistics** - View total number of questions in the database
- **User-friendly Interface** - Clean, responsive design for easy question creation

#### For Students
- **Simple Test Access** - One-click exam start without complex registration
- **Multiple Choice Questions** - Clear, easy-to-read question format
- **Instant Results** - Immediate score calculation and percentage display
- **Responsive Design** - Works seamlessly on desktop and mobile devices

#### Technical Features
- **MongoDB Integration** - Robust NoSQL database for flexible data storage
- **Flask Web Framework** - Lightweight, scalable Python web application
- **Session Management** - Secure cookie-based authentication
- **Error Handling** - Graceful 404 error handling with redirects
- **Modern UI/UX** - Clean, professional interface with CSS3 styling

<p align="right">(<a href="#readme-top">back to top</a>)</p>

### Built With

* [Python 3.7+](https://www.python.org/downloads/)
* [Flask 2.0+](https://flask.palletsprojects.com/)
* [MongoDB 4.0+](https://www.mongodb.com/)
* [HTML5](https://developer.mozilla.org/en-US/docs/Web/HTML)
* [CSS3](https://developer.mozilla.org/en-US/docs/Web/CSS)
* [JavaScript](https://developer.mozilla.org/en-US/docs/Web/JavaScript)

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- GETTING STARTED -->
## Getting Started

This is an example of how you may give instructions on setting up your project locally.
To get a local copy up and running follow these simple example steps.

### Prerequisites

This is an example of how to list things you need to use the software and how to install them.
* Python 3.7 or higher
* MongoDB 4.0 or higher
* pip (Python package installer)

### Installation

1. Clone the repo
   ```sh
   git clone https://github.com/virtual457/Online-examination-using-mongodb.git
   ```
2. Navigate to the project directory
   ```sh
   cd Online-examination-using-mongodb
   ```
3. Install Python Dependencies
   ```sh
   pip install flask pymongo werkzeug
   ```
4. Start MongoDB
   Make sure MongoDB is running on your system:
   ```sh
   # On Windows
   net start MongoDB
   
   # On macOS/Linux
   sudo systemctl start mongod
   ```
5. Run the Application
   ```sh
   cd mongo_exam
   python mongo_exam.py
   ```
6. Access the Application
   Open your web browser and navigate to:
   ```
   http://localhost:5000
   ```

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- USAGE EXAMPLES -->
## Usage

### For Teachers

1. **Access Teacher Dashboard**
   - Navigate to `http://localhost:5000/teacher`
   - Use any email format to login (demo mode)

2. **Add Questions**
   - Enter your question in the text field
   - Provide 4 multiple-choice options (A, B, C, D)
   - Select the correct answer using the radio buttons
   - Click "Add question" to save

3. **Manage Questions**
   - View the total number of questions added
   - Use "Delete all questions" to clear the database

### For Students

1. **Start Exam**
   - Navigate to `http://localhost:5000/student`
   - Click to begin the test

2. **Take the Exam**
   - Read each question carefully
   - Select your answer from the 4 options
   - Submit when finished

3. **View Results**
   - See your score as a percentage
   - Results are calculated immediately

### Project Structure

```
Online-examination-using-mongodb/
├── mongo_exam/
│   ├── mongo_exam.py          # Main Flask application
│   ├── insert.py              # Database insertion utilities
│   ├── check.py               # Answer validation logic
│   ├── tlogin.py              # Teacher authentication
│   ├── templates/             # HTML templates
│   │   ├── base.html          # Base template with navigation
│   │   ├── index.html         # Landing page
│   │   ├── teacher.html       # Teacher dashboard
│   │   ├── student.html       # Student exam start
│   │   ├── questions.html     # Exam interface
│   │   └── submit.html        # Results page
│   ├── static/                # Static assets
│   │   ├── css/               # Stylesheets
│   │   ├── js/                # JavaScript files
│   │   └── images/            # Images and icons
│   └── programs/              # Additional utility programs
└── README.md                  # This file
```

_For more examples, please refer to the [Documentation](https://github.com/virtual457/Online-examination-using-mongodb)_

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- ROADMAP -->
## Roadmap

- [ ] User registration and authentication system
- [ ] Multiple exam categories and subjects
- [ ] Timer functionality for exams
- [ ] Detailed analytics and reporting
- [ ] Question bank management
- [ ] Export results to PDF/Excel
- [ ] Real-time notifications
- [ ] Mobile app development

See the [open issues](https://github.com/virtual457/Online-examination-using-mongodb/issues) for a full list of proposed features (and known issues).

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

### Contributing Guidelines

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE.txt` for more information.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- CONTACT -->
## Contact

Chandan Gowda K S - chandan.keelara@gmail.com

Project Link: [https://github.com/virtual457/Online-examination-using-mongodb](https://github.com/virtual457/Online-examination-using-mongodb)

Project Link: [https://github.com/virtual457/Online-examination-using-mongodb](https://github.com/virtual457/Online-examination-using-mongodb)

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- ACKNOWLEDGMENTS -->
## Acknowledgments

* [Flask community](https://flask.palletsprojects.com/) for the excellent web framework
* [MongoDB team](https://www.mongodb.com/) for the powerful NoSQL database
* [HTML5 Boilerplate](https://html5boilerplate.com/) for the responsive CSS template
* [Choose an Open Source License](https://choosealicense.com)
* [GitHub Emojis](https://gist.github.com/rxaviers/7360908)
* [Malven's Flexbox Cheatsheet](https://flexbox.malven.co/)
* [Malven's Grid Cheatsheet](https://grid.malven.co/)
* [Img Shields](https://shields.io)
* [GitHub Pages](https://pages.github.com)
* [Font Awesome](https://fontawesome.com)
* [React Icons](https://react-icons.github.io/react-icons/search.html?q=search)

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/virtual457/Online-examination-using-mongodb.svg?style=for-the-badge
[forks-shield]: https://img.shields.io/github/forks/virtual457/Online-examination-using-mongodb.svg?style=for-the-badge
[stars-shield]: https://img.shields.io/github/stars/virtual457/Online-examination-using-mongodb.svg?style=for-the-badge
[issues-shield]: https://img.shields.io/github/issues/virtual457/Online-examination-using-mongodb.svg?style=for-the-badge
[license-shield]: https://img.shields.io/github/license/virtual457/Online-examination-using-mongodb.svg?style=for-the-badge
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[contributors-url]: https://github.com/virtual457/Online-examination-using-mongodb/graphs/contributors
[forks-url]: https://github.com/virtual457/Online-examination-using-mongodb/network/members
[stars-url]: https://github.com/virtual457/Online-examination-using-mongodb/stargazers
[issues-url]: https://github.com/virtual457/Online-examination-using-mongodb/issues
[license-url]: https://github.com/virtual457/Online-examination-using-mongodb/blob/master/LICENSE.txt
[linkedin-url]: https://www.linkedin.com/in/chandan-gowda-k-s-765194186/
