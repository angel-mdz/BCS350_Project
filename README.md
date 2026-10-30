# Angel Mendez Reyes — Portfolio Web Design Document

## Project overview

A personal portfolio built with HTML, CSS, and JavaScript to introduce my software and data engineering interests, demonstrate project contributions, and support job and research opportunities. The design combines a professional single-page layout with subtle retro gaming details.

## Target audience

Employers evaluating my technical skills, research coordinators exploring my interests and experience, and peers interested in my work.

## Content strategy

The introduction establishes my identity and career goals. About and Skills summarize my background; Projects & Research presents specific contributions with screenshots or evaluation output. Contact is the primary call to action, supported by project and resume links. Team contributions, the in-progress game, and the upcoming IGNITE presentation are clearly identified.

### Content questions

### 1. What is your full name as you want it displayed professionally?

Angel Mendez Reyes.

### 2. What is the purpose of your portfolio website?

My portfolio introduces my skills, projects, and research interests to support job and research opportunities. It also communicates my interest in an MS or PhD in Computer Science.

### 3. Who is the target audience (employers, clients, peers, etc.)?

Employers, research coordinators, and peers.

### 4. What skills do you want to highlight?

Backend endpoint development, MongoDB data operations, and integration with Gemini and Claude APIs, supported by organized teamwork and step-by-step problem-solving.

### 5. What projects or work will you showcase?

- **Soft Steps:** A SURI summer 2026 mental wellness app prototype. I developed FastAPI endpoints connecting MongoDB and Gemini, with Expo/React on the frontend. [Source repository](https://github.com/michellemorales/soft_steps_app).
- **SMS Spam Classifier:** An introductory Python/scikit-learn project involving data preparation, Naive Bayes training, and evaluation. Saved results on 1,115 test messages show 97.76% accuracy, 95.59% spam precision, and 87.25% spam recall.
- **2D Mystery Game (in progress):** A class project using Godot, Django, MongoDB, and Claude. My responsibility is designing endpoints connecting the game, database, and AI service. [Source repository](https://github.com/ethanmiku/CSC325_CAPSTONE).

### 6. How will you describe yourself in a short professional bio?

I am a college junior majoring in Computer Programming and Information Systems with a minor in Data Science. I enjoy understanding how software works behind the scenes and finding solutions to problems. My organized, step-by-step approach draws me toward software engineering, where I can combine careful planning with hands-on problem-solving.

### 7. What pages will your site include (Home, About, Projects, Contact, etc.)?

One scrolling page with Home, About, Skills, Projects & Research, and Contact sections.

### 8. What is your career goal or desired role?

To become a Software Engineer or Data Engineer.

### 9. What technologies or tools do you have experience with?

Python and Java; exposure to JavaScript and TypeScript; HTML and CSS; FastAPI, Django REST Framework, MongoDB, and Expo for iOS development.

### 10. What achievements or experiences are worth highlighting?

SURI undergraduate research during summer 2026, contributing to Soft Steps, and an upcoming IGNITE research presentation in spring 2027.

### 11. What call-to-action should visitors take (contact you, view projects, download resume)?

Contact me about job or research opportunities. Viewing projects and accessing my resume are supporting actions.

### 12. Will you include a resume? In what format?

Yes. About includes an HTML education and research summary, plus links to view or download my [full resume as a PDF](assets/resume/Resume_Angel.pdf).

### 13. What social or professional links will you include (GitHub, LinkedIn, etc.)?

- [GitHub](https://github.com/angel-mdz)
- [LinkedIn](https://www.linkedin.com/in/angel-mendez-36b91742b/)
- [Email: mendaj@farmingdale.edu](mailto:mendaj@farmingdale.edu)

## Information organization

| Section | Purpose |
| --- | --- |
| Home | Name, career introduction, contact/project actions, and PC illustration |
| About | Bio, education, research experience, and resume access |
| Skills | Languages, backend/mobile tools, and working approach |
| Projects & Research | Three projects, visuals/results, contributions, and available source links |
| Contact | Email, GitHub, and LinkedIn |

Sticky navigation links directly to each section. This order moves from introduction to evidence of skills and then contact. Essential project summaries, technologies, visuals, and source links stay visible outside expandable details.

## Visual design

### Design questions

### 1. What overall style will best represent you (minimalist, creative, professional, etc.)?

Minimalist and professional with a subtle retro gaming influence through pixel headings, small icons, borders, and a cozy PC illustration.

### 2. What color scheme will you use and why?

Green-tinted charcoal provides a calm dark background; emerald reflects my favorite color and highlights navigation and actions. Light text keeps the content readable.

| Role | Color |
| --- | --- |
| Background | `#101814` |
| Panels | `#19251E` |
| Main text | `#E8F0EA` |
| Secondary text | `#A9B8AE` |
| Accent | `#34D399` |

### 3. What fonts will you use for headings and body text?

Pixelify Sans Regular (400) for headings and small accents; Inter Regular (400) for body text, with 500 for emphasis. Selective pixel typography supports the retro theme while Inter keeps longer text readable.

### 4. How will your design reflect your personality or field?

The PC illustration and pixel details reflect my interest in gaming. Clear organization and project descriptions emphasize my software and data engineering interests.

### 5. What layout will your homepage follow?

On desktop, my name, introduction, and action buttons appear on the left, with the PC illustration on the right. Mobile places the text and buttons before the illustration.

### 6. How will you organize project sections visually?

Wide, stacked entries show project summaries, technologies, visuals, and expandable contributions. Visuals alternate sides on desktop; mobile places text before visuals. Soft Steps and the game use screenshots; the classifier uses saved text output in a terminal-style panel.

### 7. Will the site be mobile-friendly? How will you ensure responsiveness?

Yes. Flexible sizing, fluid headings, wrapping navigation, and a 768 px layout breakpoint adapt the page to different widths. Two-column layouts stack on narrow screens, and images scale without cropping.

### 8. What visual hierarchy will guide visitors?

My name is the largest heading, followed by the career introduction and primary Contact Me button. Section headings, project titles, body text, and quieter captions establish the remaining hierarchy.

### 9. How will consistency be maintained across pages?

Shared CSS variables, typography, spacing, buttons, and project styles keep all five sections consistent. Alternating project visuals add variety within the same layout rules.

### 10. How will accessibility be considered (contrast, font size, readability)?

Semantic landmarks, logical headings, a skip link, visible keyboard focus, descriptive image alternatives, and native disclosure controls support access. Body text uses Inter at 18 px on desktop and 16 px on narrow screens. Text contrast against the dark surfaces exceeds 7:1, and smooth scrolling respects reduced-motion preferences.

### 11. Will you use icons, images, or illustrations? Why?

A cozy PC illustration establishes the retro theme. Four project screenshots show the Soft Steps and game prototypes; saved classifier output presents its evaluation results. Decorative pixel icons support section recognition alongside visible text headings.

### 12. What portfolio websites inspired your design?

[Gazi Jarin’s portfolio](https://www.gazijarin.com/) inspired the clean layout, dark colors, spacing, and restrained gaming influence. My portfolio uses its own layout implementation, emerald palette, illustration, and icons.

### Wireframes

- [Desktop wireframe](docs/wireframes/desktop.png): split Home layout and alternating project entries.
- [Mobile wireframe](docs/wireframes/mobile.png): text-first stacked sections and wrapping navigation.

The centered content area is limited to 1120 px. Generous spacing separates sections, while consistent headings, emerald accents, and dark panels group related information.

### Resources and credits

- Inspiration: [Gazi Jarin](https://www.gazijarin.com/).
- [Pixelify Sans](https://fonts.google.com/specimen/Pixelify+Sans): [source/license](https://github.com/eifetx/Pixelify-Sans); [included SIL OFL notice](assets/fonts/pixelify-sans-OFL.txt).
- [Inter](https://fonts.google.com/specimen/Inter): [source/license](https://github.com/rsms/inter); [included SIL OFL notice](assets/fonts/inter-OFL.txt).
- [Local font sources](assets/fonts/README.md) document the distributed font files.
- [Cozy PC illustration](assets/images/cozy-pc-concept.png): generated with OpenAI image generation for this portfolio; an illustrative scene rather than my actual equipment.
- Original pixel section icons: [About](assets/images/icon-about.svg), [Skills](assets/images/icon-skills.svg), [Projects](assets/images/icon-projects.svg), and [Contact](assets/images/icon-contact.svg).
- Soft Steps and game screenshots show the team prototypes. Classifier output comes from my saved notebook evaluation.

## Interaction/functionality

### Interactivity questions

### 1. What interactive elements will your site include (navigation menus, buttons, forms)?

Sticky section navigation, an active-section indicator, independently expandable project details, and links for contact, project source code, and resume access.

### 2. Will your site include a contact form? How will it work?

No. A visible email address and `mailto:` link open the visitor’s configured email application, providing direct contact without a backend or external form service.

### 3. What JavaScript features will you implement?

JavaScript tracks the current section using IntersectionObserver and updates one navigation link with `aria-current="location"`. Resize and scroll handling keep the indicator aligned as the layout changes. Project disclosures use native HTML rather than JavaScript.

### 4. How will users receive feedback from interactions?

The current section has emerald text and an underline. Keyboard controls have visible focus outlines. Project disclosures show Show/Hide labels and expose their expanded state through native browser semantics; several can remain open independently.

### 5. How does interactivity improve the user experience?

Persistent navigation helps visitors move through the portfolio and identify their location. Expandable contributions keep project overviews concise. Direct contact and resume links make the next action easy, while keyboard support and reduced-motion behavior improve usability.

## Technical overview

The site uses semantic HTML, responsive CSS, and vanilla JavaScript. Native anchors and `details`/`summary` remain usable without JavaScript. Local WOFF2 fonts use `font-display: swap` and system fallbacks. Relative asset paths support hosting beneath a GitHub Pages repository subpath. No framework, build step, backend, or runtime library is required.

| Path | Purpose |
| --- | --- |
| `index.html` | Content, navigation, landmarks, and native disclosures |
| `css/styles.css` | Typography, colors, responsive layouts, focus and motion styles |
| `js/main.js` | Deferred active-section navigation script |
| `assets/images/` | Illustration, icons, and project screenshots |
| `assets/fonts/` | Local fonts, licenses, and source information |
| `assets/resume/` | Resume PDF |
| `docs/wireframes/` | Desktop and mobile wireframes |

### Technical references

- [MDN: IntersectionObserver](https://developer.mozilla.org/en-US/docs/Web/API/IntersectionObserver)
- [MDN: details disclosure element](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/details)
- [MDN: reduced-motion media query](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media/prefers-reduced-motion)
- [MDN: font-display](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@font-face/font-display)
- [GitHub: creating a GitHub Pages site](https://docs.github.com/en/pages/getting-started-with-github-pages/creating-a-github-pages-site)

## Timeline/project milestones

| Date | Milestone |
| --- | --- |
| October 28–29, 2026 | Define content, audience, visual direction, and wireframes |
| October 29, 2026 | Specify interactions and technical approach; build semantic HTML |
| October 29–30, 2026 | Add responsive styling, local fonts, and active-section navigation |
| October 30, 2026 | Final review and scheduled GitHub Pages publication |
| October 30, 2026, 11:59 p.m. | Assignment submission deadline |
