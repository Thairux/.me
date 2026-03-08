---
layout: default
title: Blog
permalink: /blog/
---

<section class="blog-section">
  <p class="section-eyebrow">Writing</p>
  <h1 class="section-title">Notes from the build desk</h1>
  <p class="section-intro">Short reflections, experiments, and lessons learned while building products, refining interfaces, and exploring new ideas.</p>

  <div class="blog-posts">
    {% for post in site.posts %}
      <article class="blog-post-card">
        <h2><a href="{{ post.url | relative_url }}">{{ post.title }}</a></h2>
        <div class="post-meta">
          <time datetime="{{ post.date | date: '%Y-%m-%d' }}">{{ post.date | date: "%B %d, %Y" }}</time>
        </div>
        {% if post.excerpt %}
          <p>{{ post.excerpt }}</p>
        {% endif %}
        <a href="{{ post.url | relative_url }}" class="read-more">Read More →</a>
      </article>
    {% endfor %}
  </div>
</section>
