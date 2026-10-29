# BCS350_Project

## Project overview

Personal portfolio for Angel Mendez Reyes. Phases 1-3 of this Web Design Document are complete and approved: content, visual design, interactivity, technical approach, verification plan, and milestones. Website implementation has not started. Missing personal assets and public-sharing confirmations remain explicit follow-up tasks.

## Content questions

### 1. What is your full name as you want it displayed professionally?

Angel Mendez Reyes.

### 2. What is the purpose of your portfolio website?

My portfolio will serve as a professional introduction, showcasing my skills and projects to support job and research opportunities. It will also communicate my interest in pursuing an MS or PhD in Computer Science.

### 3. Who is the target audience (employers, clients, peers, etc.)?

Employers, research coordinators, and peers.

### 4. What skills do you want to highlight?

I have experience designing backend endpoints, particularly those that integrate external AI services such as Gemini and Claude. I value organized teamwork with clear goals. I approach larger problems by creating a plan, breaking the work into manageable steps, and tracking progress.

### 5. What projects or work will you showcase?

- **Soft Steps:** Contributed to a mental wellness mobile app prototype through the SURI program under OURS at Farmingdale State College during summer 2026. I developed backend endpoints that communicated with MongoDB and the Gemini API, gaining full-stack development experience with Expo, React, and FastAPI.
- **SMS Spam Classifier:** Built an introductory machine learning project using Python and scikit-learn. I prepared data, trained a Naive Bayes classifier, and evaluated its performance.
- **2D Mystery Game — in progress:** Contributing to a class project using Godot and a Django backend with MongoDB and Claude integration. I am responsible for designing endpoints that handle HTTP requests from Godot, communicate with MongoDB, and call Claude.

### 6. How will you describe yourself in a short professional bio?

I am a college junior majoring in Computer Programming and Information Systems with a minor in Data Science. I enjoy understanding how software works behind the scenes and the challenge of finding solutions to problems. My organized, step-by-step approach draws me toward software engineering, where I can combine careful planning with hands-on problem-solving.

### 7. What pages will your site include (Home, About, Projects, Contact, etc.)?

The portfolio will use a single scrolling page with Home, About, Skills, Projects & Research, and Contact sections.

### 8. What is your career goal or desired role?

To become a Software Engineer or Data Engineer.

### 9. What technologies or tools do you have experience with?

I know Python and Java, have exposure to JavaScript and TypeScript, and am currently learning HTML and CSS. My backend experience includes FastAPI, Django REST Framework, and MongoDB, including its integration with Django. I have also used Expo for iOS app development.

### 10. What achievements or experiences are worth highlighting?

I participated in the SURI program under OURS at Farmingdale State College during summer 2026, contributing to Soft Steps. I am scheduled to present the outcomes of my research at the IGNITE conference in spring 2027.

### 11. What call-to-action should visitors take (contact you, view projects, download resume)?

The primary action is to contact me about job or research opportunities. Viewing my projects and accessing my resume are also important supporting actions. A concise HTML resume summary in About will be paired with access to the full PDF.

### 12. Will you include a resume? In what format?

Yes. The About section will include a concise education and experience summary as HTML text, with a link to view or download my full resume as a PDF. This keeps key information readable within the scrolling page while providing the complete document. The resume file still needs to be provided; the summary will be based on approved content and the supplied resume.

### 13. What social or professional links will you include (GitHub, LinkedIn, etc.)?

- GitHub: https://github.com/angel-mdz
- LinkedIn: https://www.linkedin.com/in/angel-mendez-36b91742b/
- Email: [mendaj@farmingdale.edu](mailto:mendaj@farmingdale.edu)

These contact details were supplied by the user; external profiles have not yet been verified.

## Target audience

Employers, research coordinators, and peers seeking to understand my skills, project contributions, and career interests.

## Content strategy

Introduce my software and data engineering interests, demonstrate my skills through project and research contributions, and make it easy to contact me about opportunities. Project descriptions will distinguish my contributions from team work and identify work that is still in progress. The planned IGNITE presentation will remain labeled as upcoming until completed.

## Information organization

Use one scrolling page in this order: Home, About, Skills, Projects & Research, Contact. Visitors can learn who I am, review my experience and work, and contact me about opportunities. Project viewing and resume access will support the primary contact action; About will include the resume summary and access to the full PDF.

## Content and asset follow-up tasks

- [ ] Obtain the existing resume PDF and confirm the education and experience summary before implementation.
- [ ] Collect repository or demo URLs for each project where available; confirm whether each can be shared publicly.
- [ ] Collect available project screenshots or other approved visuals during design planning; record any projects without suitable images.
- [ ] Verify supplied professional links before publication.

## Design questions

### 1. What overall style will best represent you (minimalist, creative, professional, etc.)?

A minimalist portfolio with a retro gaming influence, expressed through selective pixel typography, section icons, subtle pixel borders, and the approved cozy PC illustration.

### 2. What color scheme will you use and why?

The working palette uses green-tinted charcoal with emerald accents, reflecting my favorite color and supporting the cozy retro theme. This palette is approved for now and can be revisited after reviewing the full design.

| Role | Color |
| --- | --- |
| Background | `#101814` |
| Panels | `#19251E` |
| Main text | `#E8F0EA` |
| Secondary text | `#A9B8AE` |
| Emerald accent | `#34D399` |

The primary Contact Me button will use an emerald fill with dark text; supporting actions will use quieter emerald outlines or text. Solid-color text contrast has been checked mathematically; rendered focus states, controls, and other combinations still need verification during implementation.

### 3. What fonts will you use for headings and body text?

Slimmer pixel-style lettering is the working choice for headings and occasional small accents, and can be revisited after visual review. Body text will use a simple, readable font so longer descriptions remain easy to read. Approved font pairing: Pixelify Sans Regular (400) for headings and small accents, with Inter Regular (400) for body text.

### 4. How will your design reflect your personality or field?

Subtle retro gaming touches will reflect my interest in gaming, while the minimalist presentation will keep my skills, projects, and research easy to explore. Pixel-style typography will be used selectively rather than throughout the page.

### 5. What layout will your homepage follow?

The Home section will use a split layout, with my name, introduction, and action buttons on the left and the approved original cozy PC illustration on the right. On mobile, the introduction and action buttons will appear first, followed by the PC scene.

### 6. How will you organize project sections visually?

Projects will appear as wider, stacked entries with room for project visuals, descriptions, and my individual contributions. Screenshots are available for Soft Steps and the 2D Mystery Game but have not yet been supplied or reviewed. The SMS Spam Classifier produces text output and has no GUI; a short example of its actual output will be shown in a terminal-style panel alongside its description. The output still needs to be supplied and reviewed. On desktop, successive entries will alternate the visual and description between the left and right sides. On mobile, each project will show its title and description first, followed by its screenshot or terminal panel.

### 7. Will the site be mobile-friendly? How will you ensure responsiveness?

Yes. The desktop Home section will use text on the left and a visual on the right, while project entries will alternate visual/text sides. On mobile, Home will stack the introduction and buttons before the PC scene. Each project will stack its title and description before its screenshot or terminal panel. Breakpoints, flexible sizing, and checks for readability and overflow remain to be specified and verified during implementation.

### 8. What visual hierarchy will guide visitors?

My name will be the largest text in Home, followed by a short career introduction. Contact Me will be the primary button, with View Projects and resume access as supporting actions. The emphasis should remain harmonious with the dark and emerald theme, avoiding jarring contrast between elements. The working palette uses green-tinted charcoal and emerald; rendered states and control contrast still need verification during implementation.

### 9. How will consistency be maintained across pages?

The single-page portfolio will use shared pixel-style headings, spacing rules, button styles, and subtle pixel borders across its sections. Alternating desktop project layouts will provide variety within these consistent visual rules.

### 10. How will accessibility be considered (contrast, font size, readability)?

Body text will use a readable font, with pixel typography reserved for headings and small accents. Keyboard focus will be visible, informative images will have descriptive alternatives, and decorative artwork will be treated appropriately for assistive technology. Motion will be minimal and respect reduced-motion preferences. Exact font sizes remain to be selected. Main text, secondary text, and emerald text have been checked against both planned dark surfaces; implementation will also require keyboard and responsive readability checks.

### 11. Will you use icons, images, or illustrations? Why?

A small retro scene of a cozy PC setup in the Home section will support the gaming influence. Available screenshots of Soft Steps and the 2D Mystery Game can help visitors understand those projects. The SMS Spam Classifier will use a terminal-style panel showing a short example of actual text output alongside its description. Project screenshots and classifier output still need to be supplied and reviewed. Small pixel-style icons will accompany section headings. The original cozy PC illustration and four pixel-style section icons have been created and approved. Any external replacements will require suitable licensing and credit, and resources used in creating the artwork will be documented.

### 12. What portfolio websites inspired your design?

[Gazi Jarin's portfolio](https://www.gazijarin.com/) is a user-selected inspiration reference. Its dark presentation, generous spacing, prominent introduction, restrained bright accents, and simple section navigation offer useful reference points. The clean layout and colors are the main inspiration; the game elements also appeal to me as a secondary influence. My design will keep gaming details subtle to preserve minimalism. My portfolio will retain its approved original direction: green-tinted charcoal, emerald accents, selective slim pixel lettering, a cozy PC illustration, left-side Home text, and alternating wide project entries. A separate Game Mode is excluded; selected interactions are active-section navigation and expandable projects. The implementation, artwork, and content will be original.

## Visual design

### Approved Phase 2 design package

The established design direction is minimalist retro with the approved green-tinted charcoal/emerald palette. The user approved the desktop/mobile wireframes and Pixelify Sans + Inter font pairing. The saved illustration and original icons are also approved. Phase 2 design planning is complete; implementation and rendered accessibility verification remain for later phases.

- Approved typography: **Pixelify Sans Regular (400)** for headings and small accents, **Inter Regular (400)** for body text; 500 for occasional emphasis. [Font sample](docs/design/font-sample.html). Fonts will be hosted locally with their license notices.
- [Desktop wireframe](docs/wireframes/desktop.png): split Home, wide alternating projects, About resume access, and Contact section.
- [Mobile wireframe](docs/wireframes/mobile.png): Home text/buttons before artwork; project text before visuals. Navigation uses wrapping links and stays visible during scrolling, as approved in Phase 3.
- [Original cozy PC concept](docs/design/cozy-pc-concept.png): the approved AI-generated illustration is saved and placed in both wireframes. It follows the same cozy PC direction as the earlier concept. It is illustrative rather than a depiction of the user's actual equipment.
- Approved section icons: original small pixel motifs (person, code brackets, folder, envelope), paired with visible headings. [Icon review sheet](docs/design/pixel-icons.png). Individual currentColor SVGs are saved as docs/design/icon-about.svg, icon-skills.svg, icon-projects.svg, and icon-contact.svg. The low-fidelity wireframes retain square placement markers; the actual illustration and SVG icon designs are approved.

Wireframes show content roles where actual assets are missing; no project results, screenshots, or classifier output have been fabricated. These are planning drawings, not implemented pages. Layout content is indicative; approved content answers remain authoritative.

### Proposed reusable rules

Use a centered content area up to approximately 1120 px with generous section spacing. Body text starts at 18 px with approximately 1.6 line height; narrow screens may use 16 px. Use fluid pixel headings, short lines, and a spacing scale of 8, 16, 24, 32, 48, and 64 px. At widths where two columns no longer fit comfortably (initial planning point: 768 px), stack the Home and project layouts. Validate intermediate widths rather than treating this breakpoint as verified.

Use semantic landmarks, ordered headings, and a skip link. Keep logical reading order consistent even when desktop visual sides alternate. Proposed focus treatment: a 2 px emerald outline with offset against dark surfaces; emerald-filled controls need a contrasting dark separation. Maintain descriptive text labels, decorative icons hidden from assistive technology, and no essential information conveyed only by color. Avoid autoplay and respect reduced-motion preferences.

Calculated contrast ratios against background / panel respectively: main text 15.55 / 13.65, secondary text 8.73 / 7.67, emerald 9.39 / 8.25. Dark text on the emerald button is 9.39. These are solid-color calculations, not rendered accessibility verification.

### Resources and asset responsibilities

- Inspiration: [Gazi Jarin](https://www.gazijarin.com/), especially clean spacing and restrained dark/bright colors. No source code or artwork copied.
- [Pixelify Sans](https://fonts.google.com/specimen/Pixelify+Sans), [source and SIL OFL 1.1 license](https://github.com/eifetx/Pixelify-Sans).
- [Inter](https://fonts.google.com/specimen/Inter), [source and SIL OFL 1.1 license](https://github.com/rsms/inter).
- If fonts are distributed with the website, retain their license/copyright notices. No font files have been added yet.
- Approved original illustration generated with OpenAI image generation. Approved original section icons were drawn for this project, without an external icon dependency.
- Soft Steps/game screenshots, actual classifier output, resume PDF, and public-sharing confirmation remain user asset follow-ups before implementation/publication.

## Interactivity questions

### 1. What interactive elements will your site include (navigation menus, buttons, forms)?

Section navigation with an active-section indicator, expandable project details, and links for contact, project resources, and resume access. Navigation stays visible while scrolling, with wrapping links on mobile. Each project initially shows its summary, technologies, and visual; visitors can expand additional approved information. A separate Game Mode, copy-email button, and PC screen toggle are not included in the selected feature set.

### 2. Will your site include a contact form? How will it work?

No contact form. Visitors will use an email link to mendaj@farmingdale.edu, which asks their device to open its configured email application. The address will also remain visible for manual use. No external form service or copy-email button is planned.

### 3. What JavaScript features will you implement?

JavaScript will track the current section as visitors scroll and update its navigation indicator using IntersectionObserver. Project details will use native HTML details/summary controls, so expansion does not depend on JavaScript. CSS will provide smooth section scrolling unless the visitor prefers reduced motion. No form processing or game functionality is planned.

### 4. How will users receive feedback from interactions?

The current navigation link will use emerald text and an underline, so its state is not conveyed by color alone. Project controls will change between "Show details" and "Hide details," with expanded/collapsed states available to assistive technology. Controls will support keyboard use and visible focus. Multiple projects can remain expanded at once. The email link opens the visitor's configured email application; the website will not claim that a message has been sent.

### 5. How does interactivity improve the user experience?

Persistent section navigation and the active-section indicator help visitors move through the single-page portfolio and understand their location. Expandable details keep the initial project overview concise while allowing visitors to explore my contributions and additional approved information. Email-link contact provides a direct way to reach me about opportunities. Keyboard support, visible states, and reduced-motion behavior make these interactions usable by more visitors.

## Interaction/functionality

Approved navigation remains visible during scrolling and uses wrapping links on mobile. The current section is identified with emerald text and an underline. In-page navigation uses smooth scrolling unless reduced motion is preferred.

Projects initially display their summary, technologies, and visual. "Show details" reveals individual contributions and additional approved information; the control changes to "Hide details" when expanded. Multiple entries may remain expanded. Controls must support keyboard use, visible focus, and accessible expanded/collapsed states.

Contact uses an email link with the address visible for manual use. No contact form, external submission service, or separate Game Mode is planned. The technical and verification plans below are approved; implementation remains paused until requested.

## Technical overview

Approved setup: original semantic HTML, CSS, and vanilla JavaScript, with separate stylesheet/script files and locally hosted fonts. No framework, package manager, build step, backend, external form service, or JavaScript library is needed. Browser features will provide the small interaction set. The existing Python scripts under docs/design reproduce planning assets; they are not website runtime dependencies.

### File organization and font delivery

The following paths are planned; website files have not been created yet.

| Path | Purpose |
| --- | --- |
| `index.html` | Single page with Home, About, Skills, Projects & Research, Contact |
| `css/styles.css` | Shared design rules, layouts, responsive and interaction states |
| `js/main.js` | Active-section tracking and any small interaction enhancements |
| `assets/images/` | Approved artwork, SVG icons, and supplied project screenshots |
| `assets/fonts/` | Pixelify Sans 400 and Inter 400/500 font files with license notices |
| `assets/resume/` | Supplied and approved public resume PDF |
| `docs/` | Existing wireframes and design source/review assets |

Use lowercase, hyphenated asset names and relative URLs that work under the repository's GitHub Pages subpath. CSS font/image paths resolve relative to the stylesheet. Retain approved planning assets under docs; prepare appropriately sized website copies during implementation. Do not create fake screenshots, classifier output, resume content, or project links.

Fonts will use local WOFF2 files, `@font-face`, `font-display: swap`, and suitable system fallbacks. Retain the original font license and copyright notices. Font acquisition and loading checks are implementation tasks, not completed work.

### Approved implementation plan

- Use real section-anchor links and a sticky header. Account for its wrapped height when positioning anchor targets so headings and keyboard focus are not obscured. Preserve normal URL hashes and browser Back behavior.
- Use IntersectionObserver for active-section tracking, with one current link marked visually and with `aria-current="location"`. Recalculate for viewport/header changes and expanded project content; verify short sections and the bottom Contact section. Passive scrolling must not move keyboard focus or generate repeated live announcements. Without JavaScript, ordinary section navigation remains usable without a dynamic indicator.
- Use native `details`/`summary` for independent project disclosures, initially collapsed, with Show/Hide labels reflecting the open state. Native disclosure behavior provides keyboard operation and expanded state without a custom widget. Keep essential summaries, technologies, visuals, and resource links outside the collapsed details. No exclusive accordion group. Verify actual screen-reader output before claiming accessibility.
- Tab/Shift+Tab follow the document order; Enter activates links; Enter/Space toggle project disclosures. Focus remains on the disclosure control when toggled. No custom arrow-key scheme or focus trap is needed. A skip link reaches main content.
- Use CSS smooth scrolling only when reduced motion is not requested; project expansion need not animate. Do not intercept normal email, resume, or external-link behavior.

### Technical references

- [MDN: IntersectionObserver](https://developer.mozilla.org/en-US/docs/Web/API/IntersectionObserver)
- [MDN: details disclosure element](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/details)
- [MDN: reduced-motion media query](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media/prefers-reduced-motion)
- [MDN: font-display](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@font-face/font-display)
- [GitHub: creating a GitHub Pages site](https://docs.github.com/en/pages/getting-started-with-github-pages/creating-a-github-pages-site)

## Verification plan

Approved checks for implementation and publication; none have been run against a website yet.

| Area | Checks |
| --- | --- |
| Content and document | Confirm all 30 answers and required sections, actual project contributions, upcoming/in-progress labels, resource credits, and approved assets |
| Layout | Check approximately 320, 375, 768, 1024, and 1440 px widths plus intermediate resizing; text-first mobile order; no unintended horizontal overflow; readable text at 200% zoom |
| Keyboard and accessibility | Complete keyboard journey, skip link, visible/unobscured focus, disclosure Enter/Space behavior, logical headings/landmarks, meaningful alternatives, accessible disclosure state, current-link state, contrast and reduced motion |
| Interactions | Scroll and click through every section in both directions; direct hash loads and Back; active indicator after resizing and expanding projects; open multiple projects and close independently |
| Resilience | Disable JavaScript and block font loading: content, anchors, disclosures, email, and resume access remain usable; fallback text remains readable |
| Assets and links | Check exact filename case, relative paths, font licenses, no broken requests, actual classifier output, resume view/download, and supplied professional/project URLs |
| Browser and live site | Check in available Chromium and Firefox browsers; test touch/narrow layouts and note device limitations; inspect console/network errors; after authorized publishing, repeat essential checks on the actual GitHub Pages URL |

Record actual results and limitations during implementation. Planning contrast calculations and design reviews are not substitutes for these checks.

## Timeline/project milestones

User-supplied deadline: **October 30, 2026, at 11:59 p.m.** Eastern time is assumed from the user's local timezone; confirm if the course specifies otherwise. The following is the approved target schedule, not a record of completed implementation work. Final planning review was approved October 29; asset intake remains outstanding.

| Target | Milestone and completion condition |
| --- | --- |
| October 29 | Final planning review and asset intake: agree on technical/verification plan; obtain resume, screenshots, classifier output, URLs, and public-sharing confirmations |
| October 29-30 | Phase 4: semantic page and approved content, usable anchors and native disclosures; review and focused commit when authorized |
| October 30 | Phase 5: approved responsive design, local fonts, and accessible states; review and focused commits when authorized |
| October 30 | Phase 6: active-section JavaScript and interaction checks; review and focused commit when authorized |
| October 30, before submission | Phase 7: complete verification, fix issues, obtain push/publication authorization, verify live site, and finalize README with repository/live URLs |
| October 30, before 11:59 p.m. | User submits the two verified URLs to Brightspace; leave time for deployment and corrections |

Missing assets or permissions must be resolved or explicitly re-scoped with the user. Website implementation has not begun and remains paused until requested.
