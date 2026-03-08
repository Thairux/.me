---
layout: default
title: Home
---

{% assign latest_post = site.posts.first %}
{% assign featured_projects = site.projects | sort: "order" %}

<section class="hero-intro">
  <div class="hero-copy">
    <p class="hero-badge">Minimalist modern</p>
    <h1>Building polished software with warmth, clarity, and character.</h1>
    <p class="hero-lead">I'm Thairux, and this space brings together selected projects, practical writing, and the kind of product-minded engineering work I want to keep doing more of.</p>
    <div class="hero-actions">
      <a href="{{ '/projects/' | relative_url }}" class="button-primary">Explore Projects</a>
      <a href="{{ '/about/' | relative_url }}" class="button-secondary">About Me</a>
    </div>
  </div>

  <aside class="hero-panel">
    <p class="panel-kicker">Current focus</p>
    <div class="stat-grid">
      <article class="stat-card">
        <strong>Full-stack apps</strong>
        <span>Shipping useful interfaces with reliable backend foundations.</span>
      </article>
      <article class="stat-card">
        <strong>Current stack</strong>
        <span>JavaScript, Python, Git, APIs, automation, and clean UI systems.</span>
      </article>
      <article class="stat-card">
        <strong>Current focus</strong>
        <span>Developer tools, polished web experiences, and useful product workflows.</span>
      </article>
      <article class="stat-card">
        <strong>Open to</strong>
        <span>Collaborations, thoughtful product work, and interesting technical challenges.</span>
      </article>
    </div>
  </aside>
</section>

<section class="page-section">
  <p class="section-eyebrow">Latest highlights</p>
  <h2 class="section-title">Recent work, stack notes, and what I'm exploring.</h2>
  <p class="section-intro">A quick snapshot of what's new here right now: the latest note, the tools I reach for most, and the kind of work I want this portfolio to keep reflecting.</p>

  <div class="feature-grid">
    <article class="feature-card">
      <div class="feature-card-top">
        <span class="mini-label">Latest post</span>
      </div>
      {% if latest_post %}
        <h3>{{ latest_post.title }}</h3>
        <p>{{ latest_post.excerpt | strip_html | truncate: 160 }}</p>
        <a href="{{ latest_post.url | relative_url }}" class="text-link">Read the post</a>
      {% endif %}
    </article>
    <article class="feature-card">
      <div class="feature-card-top">
        <span class="mini-label">Stack snapshot</span>
      </div>
      <h3>Tools I use most</h3>
      <p>JavaScript and Python for building, Git and GitHub for shipping, and a design-first approach to interface polish, structure, and usability.</p>
      <div class="pill-list compact">
        <span>JavaScript</span>
        <span>Python</span>
        <span>Git</span>
        <span>UI systems</span>
      </div>
    </article>
    <article class="feature-card">
      <div class="feature-card-top">
        <span class="mini-label">Current focus</span>
      </div>
      <h3>HOSQ and practical product systems</h3>
      <p>Right now I'm especially interested in products like HOSQ that combine real operational needs, real-time updates, and a cleaner experience for the people using them.</p>
      <a href="{{ '/projects/hosq/' | relative_url }}" class="text-link">View the case study</a>
    </article>
  </div>
</section>

<section class="page-section">
  <p class="section-eyebrow">Selected projects</p>
  <h2 class="section-title">Projects I want people to open first.</h2>
  <p class="section-intro">A few focused examples that show how I think about product clarity, technical structure, and building things that feel genuinely useful.</p>

  <div class="project-grid">
    {% for project in featured_projects limit: 3 %}
      <article class="project-card">
        <div class="project-visual {{ project.visual_class | default: 'project-visual-notes' }}">
          <span class="project-visual-label">{{ project.badge | default: 'Project' }}</span>
        </div>
        <div class="card-topline">{{ project.label | default: 'Featured project' }}</div>
        <h3><a href="{{ project.url | relative_url }}" class="project-title-link">{{ project.title }}</a></h3>
        <p>{{ project.description }}</p>
        <div class="pill-list compact">
          {% for tech in project.technologies limit: 4 %}
            <span>{{ tech }}</span>
          {% endfor %}
        </div>
        <div class="project-links-inline">
          <a href="{{ project.url | relative_url }}">Read case study</a>
          {% if project.demo %}
            <a href="{{ project.demo }}" target="_blank" rel="noopener noreferrer">Live site</a>
          {% endif %}
        </div>
      </article>
    {% endfor %}
  </div>
</section>

<section class="page-section">
  <p class="section-eyebrow">Skills & stack</p>
  <h2 class="section-title">What I use to design, build, and ship.</h2>
  <div class="feature-grid">
    <article class="feature-card">
      <div class="feature-card-top">
        <span class="mini-label">Frontend</span>
      </div>
      <h3>Interfaces with clarity</h3>
      <p>I like building interfaces that feel calm, readable, and fast to understand.</p>
      <div class="pill-list compact">
        <span>HTML</span>
        <span>CSS</span>
        <span>JavaScript</span>
        <span>TypeScript</span>
      </div>
    </article>
    <article class="feature-card">
      <div class="feature-card-top">
        <span class="mini-label">Backend</span>
      </div>
      <h3>Reliable product logic</h3>
      <p>For application logic and connected systems, I lean toward tools that support shipping quickly without losing structure.</p>
      <div class="pill-list compact">
        <span>Python</span>
        <span>Supabase</span>
        <span>APIs</span>
        <span>Realtime data</span>
      </div>
    </article>
    <article class="feature-card">
      <div class="feature-card-top">
        <span class="mini-label">Workflow</span>
      </div>
      <h3>From idea to delivery</h3>
      <p>I enjoy the process around the code too: versioning, iteration, writing, and refining product direction over time.</p>
      <div class="pill-list compact">
        <span>Git</span>
        <span>GitHub</span>
        <span>Automation</span>
        <span>Technical writing</span>
      </div>
    </article>
  </div>
</section>

<section class="page-section">
  <p class="section-eyebrow">Contact</p>
  <h2 class="section-title">Open to useful work and thoughtful collaboration.</h2>
  <div class="content-grid">
    <article class="surface-card">
      <h2>What I'm interested in</h2>
      <ul class="styled-list">
        <li>Full-stack product engineering work</li>
        <li>Developer tooling and workflow automation</li>
        <li>UI refinement for products that need more clarity and polish</li>
        <li>Interesting collaborations with practical real-world use</li>
      </ul>
    </article>
    <article class="surface-card">
      <h2>Reach out</h2>
      <p>If you'd like to talk about a project, collaboration, or role, the easiest place to start is through GitHub or Twitter.</p>
      <div class="hero-actions contact-actions">
        <a href="https://github.com/Thairux" class="button-primary" target="_blank" rel="noopener noreferrer">GitHub</a>
        <a href="https://twitter.com/thairux" class="button-secondary" target="_blank" rel="noopener noreferrer">Twitter</a>
        <a href="{{ '/blog/' | relative_url }}" class="button-secondary">Read the Blog</a>
      </div>
    </article>
  </div>
</section>
