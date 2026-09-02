# CS180 Projects — Rajah

A very basic, plain HTML/CSS project gallery, meant to be hosted on GitHub Pages.

## Structure

```
.
├── index.html              # Home page — links to every project
├── style.css                # Shared stylesheet for the whole site
├── README.md
└── projects/
    └── 01-camera/
        ├── index.html       # Project 1 writeup
        └── media/           # Put project 1's photos/GIF here
```

## Publishing it on GitHub Pages

1. **Create a repo on GitHub.** Any name works (e.g. `cs180-projects`). Public repo,
   no need to add a README/gitignore since you already have files locally.
2. **Push these files to it:**

   ```bash
   cd cs180-site
   git init
   git add .
   git commit -m "Initial site"
   git branch -M main
   git remote add origin https://github.com/<your-username>/<your-repo>.git
   git push -u origin main
   ```

3. **Turn on Pages:** on GitHub, go to the repo's **Settings → Pages**. Under
   "Build and deployment," set **Source** to `Deploy from a branch`, pick the
   `main` branch and `/ (root)` folder, then Save.
4. After a minute or two, your site will be live at:

   ```
   https://<your-username>.github.io/<your-repo>/
   ```

   GitHub shows the exact URL on that same Settings → Pages screen once it's
   deployed.

## Adding Project 1's photos

Drop your images/GIF into `projects/01-camera/media/`, then open
`projects/01-camera/index.html` and, for each placeholder, swap the
`<div class="placeholder">...</div>` for the commented-out `<img>` tag right
below it (just uncomment it and point `src` at your file, e.g.
`media/part1-close.jpg`).

## Adding a future project

1. Duplicate the `projects/01-camera/` folder, rename it (e.g. `projects/02-name/`).
2. Edit its `index.html` with that project's content.
3. Add a new card to the `.project-grid` in the top-level `index.html`:

   ```html
   <a class="project-card" href="projects/02-name/index.html">
     <h3>Project 2</h3>
     <p>Short description.</p>
     <span class="tag">Due date</span>
   </a>
   ```

That's it — no build step, no framework, just static files.
