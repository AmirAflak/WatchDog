<!-- Improved compatibility of back to top link: See: https://github.com/othneildrew/Best-README-Template/pull/73 -->
<a name="readme-top"></a>
<!--
*** Thanks for checking out the Best-README-Template. If you have a suggestion
*** that would make this better, please fork the repo and create a pull request
*** or simply open an issue with the tag "enhancement".
*** Don't forget to give the project a star!
*** Thanks again! Now go create something AMAZING! :D
-->



<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->
[![MIT License][license-shield]][license-url]



<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="[https://github.com/AmirAflak/WatchDog">
    <img src="images/logo.jpeg" alt="Logo" width="80" height="80">
  </a>

  <h3 align="center">WatchDog</h3>

  <p align="center">
    powerful ETL subdomain tracking pipeline
   </p>
</div>



<!-- ABOUT THE PROJECT -->
## About The Project
Watchdog is a powerful ETL pipeline designed to track subdomains of specified domains. It employs multiprocessing for efficient subdomain generation, Kafka for seamless streaming, MongoDB for scalable storage, PySpark for advanced subdomain processing, and Airflow for robust orchestration.

## Features
* <b>Efficient Subdomain Generation:</b> Watchdog leverages multiprocessing to generate subdomains quickly and accurately, optimizing performance.
* <b>Real-time Streaming:</b> The pipeline integrates Kafka to provide seamless and reliable data streaming, ensuring up-to-date information.
* <b>Scalable Storage:</b> Watchdog utilizes MongoDB as its storage solution, enabling flexible and scalable management of subdomains.
* <b>Advanced Subdomain Processing:</b> With the power of PySpark, Watchdog efficiently processes and analyzes subdomains, allowing for sophisticated data manipulation.
* <b>Robust Orchestration:</b> Watchdog employs Airflow for effective workflow management and task coordination, ensuring smooth execution.

### Built With
* [Apache Airflow](https://airflow.apache.org/) - Workflow management and task scheduling.
* [Apache Spark](https://spark.apache.org/) - Fast and distributed data processing.
* [Apache Kafka](https://kafka.apache.org/) - Distributed streaming platform.
* [MongoDB](https://www.mongodb.com/) - Scalable NoSQL database.
  

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- GETTING STARTED -->
## Getting Started

This is an example of how you may give instructions on setting up your WatchDog locally.
To get a local copy up and running follow these simple example steps.

### Prerequisites
Before you can use this project, you'll need to have the following installed on your machine:
* Python above 3.10
* Docker
* Docker Compose
* Airflow

If you don't have these installed, you can follow the installation instructions for each tool:
* [Install Docker](https://docs.docker.com/get-docker/)
* [Install Docker Compose](https://docs.docker.com/compose/install/)
* [Install Airflow](https://airflow.apache.org/docs/apache-airflow/stable/installation/index.html)

Once you have these tools installed, you'll be ready to use this project.

### Installation

1. Clone the repo
   ```sh
   git clone https://github.com/AmirAflak/WatchDog.git
   ```
2. Navigate to the project directory:
   ```sh
   cd WatchDog/
   ```
3. Set targets in configs.py:
   ```py
   TARGETS=['caterpillar.com', 'url.com']
   ```
4. Install the required packages:
   ```sh
   make install
   ``` 
5. Initialize Docker Compose:
   ```sh
   make docker
   ```
6. Initialize the Spark streaming consumer:
   ```sh
   make consumer
   ```
7. Initialize the Airflow scheduler:
   ```sh
   make scheduler
   ```
8. Initialize the Airflow webserver GUI:
   ```sh
   make webserver
   ```
9. To stop the Docker Compose containers, run:
   ```sh
   make stop
   ```
That's it! You should now be able to use the project.


<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- USAGE EXAMPLES -->
## Usage

Use this space to show useful examples of how a project can be used. Additional screenshots, code examples and demos work well in this space. You may also link to more resources.

_For more examples, please refer to the [Documentation](https://example.com)_

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

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE.txt` for more information.



<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/othneildrew/Best-README-Template.svg?style=for-the-badge
[contributors-url]: https://github.com/othneildrew/Best-README-Template/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/othneildrew/Best-README-Template.svg?style=for-the-badge
[forks-url]: https://github.com/othneildrew/Best-README-Template/network/members
[stars-shield]: https://img.shields.io/github/stars/othneildrew/Best-README-Template.svg?style=for-the-badge
[stars-url]: https://github.com/othneildrew/Best-README-Template/stargazers
[issues-shield]: https://img.shields.io/github/issues/othneildrew/Best-README-Template.svg?style=for-the-badge
[issues-url]: https://github.com/othneildrew/Best-README-Template/issues
[license-shield]: https://img.shields.io/github/license/othneildrew/Best-README-Template.svg?style=for-the-badge
[license-url]: https://github.com/othneildrew/Best-README-Template/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/othneildrew
[product-screenshot]: images/screenshot.png
[Next.js]: https://img.shields.io/badge/next.js-000000?style=for-the-badge&logo=nextdotjs&logoColor=white
[Next-url]: https://nextjs.org/
[React.js]: https://img.shields.io/badge/React-20232A?style=for-the-badge&logo=react&logoColor=61DAFB
[React-url]: https://reactjs.org/
[Vue.js]: https://img.shields.io/badge/Vue.js-35495E?style=for-the-badge&logo=vuedotjs&logoColor=4FC08D
[Vue-url]: https://vuejs.org/
[Angular.io]: https://img.shields.io/badge/Angular-DD0031?style=for-the-badge&logo=angular&logoColor=white
[Angular-url]: https://angular.io/
[Svelte.dev]: https://img.shields.io/badge/Svelte-4A4A55?style=for-the-badge&logo=svelte&logoColor=FF3E00
[Svelte-url]: https://svelte.dev/
[Laravel.com]: https://img.shields.io/badge/Laravel-FF2D20?style=for-the-badge&logo=laravel&logoColor=white
[Laravel-url]: https://laravel.com
[Bootstrap.com]: https://img.shields.io/badge/Bootstrap-563D7C?style=for-the-badge&logo=bootstrap&logoColor=white
[Bootstrap-url]: https://getbootstrap.com
[JQuery.com]: https://img.shields.io/badge/jQuery-0769AD?style=for-the-badge&logo=jquery&logoColor=white
[JQuery-url]: https://jquery.com 
