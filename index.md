---
layout: default
title: Home
---

{% include hero.html %}

<section id="about" class="section">
  <div class="container">
    <h2>About Me</h2>
    <div class="about-content">
      <p>Welcome to my portfolio! I'm a passionate developer who loves creating innovative solutions and building meaningful projects.</p>
      <p>Feel free to explore my work, skills, and experience below.</p>
    </div>
  </div>
</section>

<section id="projects" class="section">
  <div class="container">
    <h2>Projects</h2>
    <div class="projects-grid">
      {% for project in site.projects %}
        <div class="project-card">
          <h3>{{ project.title }}</h3>
          <p>{{ project.description }}</p>
          {% if project.technologies %}
            <div class="technologies">
              {% for tech in project.technologies %}
                <span class="tech-tag">{{ tech }}</span>
              {% endfor %}
            </div>
          {% endif %}
          {% if project.github %}
            <a href="{{ project.github }}" class="project-link" target="_blank">View on GitHub</a>
          {% endif %}
          {% if project.demo %}
            <a href="{{ project.demo }}" class="project-link" target="_blank">Live Demo</a>
          {% endif %}
        </div>
      {% endfor %}
    </div>
  </div>
</section>

<section id="skills" class="section">
  <div class="container">
    <h2>Skills</h2>
    <div class="skills-grid">
      {% for category in site.data.skills %}
        <div class="skill-category">
          <h3>{{ category.name }}</h3>
          <ul class="skill-list">
            {% for skill in category.items %}
              <li>{{ skill }}</li>
            {% endfor %}
          </ul>
        </div>
      {% endfor %}
    </div>
  </div>
</section>

<section id="experience" class="section">
  <div class="container">
    <h2>Experience</h2>
    <div class="experience-list">
      {% for experience in site.data.experience %}
        <div class="experience-item">
          <div class="experience-header">
            <h3>{{ experience.title }}</h3>
            <span class="experience-date">{{ experience.date }}</span>
          </div>
          <p class="experience-company">{{ experience.company }}</p>
          <p class="experience-description">{{ experience.description }}</p>
        </div>
      {% endfor %}
    </div>
  </div>
</section>

<section id="education" class="section">
  <div class="container">
    <h2>Education</h2>
    <div class="education-list">
      {% for education in site.data.education %}
        <div class="education-item">
          <div class="education-header">
            <h3>{{ education.degree }}</h3>
            <span class="education-date">{{ education.date }}</span>
          </div>
          <p class="education-institution">{{ education.institution }}</p>
          {% if education.description %}
            <p class="education-description">{{ education.description }}</p>
          {% endif %}
        </div>
      {% endfor %}
    </div>
  </div>
</section>

<section id="contact" class="section">
  <div class="container">
    <h2>Contact</h2>
    <div class="contact-content">
      <p>Feel free to reach out if you'd like to collaborate or have any questions!</p>
      <div class="contact-links">
        {% if site.social.email %}
          <a href="mailto:{{ site.social.email }}" class="contact-link">Email</a>
        {% endif %}
        {% if site.social.github %}
          <a href="{{ site.social.github }}" class="contact-link" target="_blank">GitHub</a>
        {% endif %}
        {% if site.social.linkedin %}
          <a href="{{ site.social.linkedin }}" class="contact-link" target="_blank">LinkedIn</a>
        {% endif %}
        {% if site.social.twitter %}
          <a href="{{ site.social.twitter }}" class="contact-link" target="_blank">Twitter</a>
        {% endif %}
      </div>
    </div>
  </div>
</section>
