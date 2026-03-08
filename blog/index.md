---
layout: default
title: Blog
---

<section class="blog-section">
  <div class="container">
    <h1>Blog</h1>
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
  </div>
</section>
