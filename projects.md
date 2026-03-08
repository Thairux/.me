---
layout: default
title: Projects
permalink: /projects/
---

<section class="page-section">
  <p class="section-eyebrow">Projects</p>
  <h1>Selected work and experiments.</h1>
  <p class="section-intro">A few highlights that reflect how I like to build: practical ideas, clean presentation, and a bias toward tools that are genuinely useful.</p>

  <div class="project-grid">
    {% assign sorted_projects = site.projects | sort: "order" %}
    {% for project in sorted_projects %}
      <article class="project-card">
        <div class="project-visual {{ project.visual_class | default: 'project-visual-notes' }}">
          <span class="project-visual-label">{{ project.badge | default: 'Project' }}</span>
        </div>
        <div class="card-topline">{{ project.label | default: 'Featured project' }}</div>
        <h2><a href="{{ project.url | relative_url }}" class="project-title-link">{{ project.title }}</a></h2>
        <p>{{ project.description }}</p>
        {% if project.technologies %}
          <div class="pill-list compact">
            {% for tech in project.technologies limit: 4 %}
              <span>{{ tech }}</span>
            {% endfor %}
          </div>
        {% endif %}
        <div class="project-links-inline">
          <a href="{{ project.url | relative_url }}">Case Study</a>
          {% if project.demo %}
            <a href="{{ project.demo }}" target="_blank" rel="noopener noreferrer">Live Site</a>
          {% endif %}
          {% if project.github %}
            <a href="{{ project.github }}" target="_blank" rel="noopener noreferrer">Repository</a>
          {% endif %}
        </div>
      </article>
    {% endfor %}
  </div>
</section>

<section class="page-section">
  <p class="section-eyebrow">Featured repositories</p>
  <h2 class="section-title">Open source work worth opening first.</h2>
  <div class="feature-grid">
    <article class="feature-card">
      <div class="feature-card-top">
        <span class="mini-label">Live now</span>
      </div>
      <h3>HOSQ</h3>
      <p>A real-time hospital queue management system with patient self-service, staff workflows, and queue visibility designed for practical use.</p>
      <a href="https://github.com/Thairux/hosq" class="text-link" target="_blank" rel="noopener noreferrer">View repository</a>
    </article>
    <article class="feature-card">
      <div class="feature-card-top">
        <span class="mini-label">Portfolio</span>
      </div>
      <h3>.me</h3>
      <p>This portfolio repository tracks the site itself, including layout refinements, writing structure, and the visual direction of the personal brand.</p>
      <a href="https://github.com/Thairux/.me" class="text-link" target="_blank" rel="noopener noreferrer">Open repository</a>
    </article>
    <article class="feature-card">
      <div class="feature-card-top">
        <span class="mini-label">More work</span>
      </div>
      <h3>GitHub profile</h3>
      <p>Browse additional experiments, works in progress, and supporting repositories that show the broader range of ideas under development.</p>
      <a href="https://github.com/Thairux" class="text-link" target="_blank" rel="noopener noreferrer">Explore GitHub</a>
    </article>
  </div>
</section>
