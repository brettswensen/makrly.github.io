# Headspace — Style Reference
> Warm Modern Playfulness — like a friendly, brightly lit studio full of soft shapes and uplifting colors.

**Theme:** light

Headspace's design system radiates a calm, approachable, and playfully optimistic mood, achieved through a vibrant primary blue, a warm, soft neutral palette, and abundant negative space. Rounded forms and a clean sans-serif typeface contribute to a friendly and user-centric feel. The frequent use of accent colors, especially yellow and various purples, in illustrations and iconography creates visual interest and distinguishes different content areas.

## Tokens — Colors

| Name | Value | Token | Role |
|------|-------|-------|------|
| Sky Connect | `#0061ef` | `--color-sky-connect` | Primary interactive elements (buttons, links, active states) — a bold commitment to guidance and support amidst the softer palette. |
| Sunshine Burst | `#ffce00` | `--color-sunshine-burst` | Accent for illustrations, banners, and hero backgrounds — injects energetic warmth and optimism. |
| Deep Plum | `#3b197f` | `--color-deep-plum` | Accent for illustrations and thematic sections — provides a rich, grounding counterpoint to brighter accents. |
| Ocean Glimmer | `#00a4ff` | `--color-ocean-glimmer` | Accent for iconography and illustrations, suggesting clarity and serenity. |
| Blush Petal | `#ffa1cc` | `--color-blush-petal` | Accent in illustrations, adding softness and a touch of playfulness. |
| Forest Calm | `#02873a` | `--color-forest-calm` | Accent in illustrations, symbolizing growth and tranquility. |
| Inkwell Gray | `#4b4c4d` | `--color-inkwell-gray` | Dominant body text, strong headings, button text — balances the soft background with clear readability. |
| True Black | `#000000` | `--color-true-black` | Highest contrast text, input text — used sparingly for emphasis. |
| Charcoal Tone | `#2d2c2b` | `--color-charcoal-tone` | Darker button backgrounds, secondary text, accents in illustrations — creates depth without harshness. |
| Cloud Whisper | `#f9f4f2` | `--color-cloud-whisper` | Light background surfaces, subtle button backgrounds — a warm, inviting default for section backgrounds and off-white elements. |
| Stone Slate | `#6b6b6b` | `--color-stone-slate` | Text on lighter backgrounds for softer contrast, icon fills. |
| Pure White | `#ffffff` | `--color-pure-white` | Card backgrounds, selected elements, high-contrast text on dark backgrounds. |
| Pale Ash | `#e2ded9` | `--color-pale-ash` | Subtle borders, button outlines, subtle shadows — defines soft separation. |
| Light Stone | `#d0d0d0` | `--color-light-stone` | Input borders, light outlines on cards. |

## Tokens — Typography

### Headspace Apercu
The primary typeface for all text content. Its clean, humanist sans-serif forms contribute to the approachable and friendly tone. Weight 700 is reserved for main headings, 500 for subheadings and important labels, and 400 for body text; specific letter-spacing adjustments at larger sizes create an open, legible feel.

- **Font Family:** Headspace Apercu, system-ui, sans-serif
- **Weights:** 400, 500, 700

### Type Scale

| Role | Size | Line Height | Letter Spacing | Token |
|------|------|-------------|----------------|-------|
| caption | 12px | 1.5 | — | --text-caption |
| body-sm | 14px | 1.44 | — | --text-body-sm |
| body | 16px | 1.38 | — | --text-body |
| subheading | 18px | 1.33 | — | --text-subheading |
| heading-sm | 24px | 1.32 | -0.48px | --text-heading-sm |
| heading | 32px | 1.29 | -0.8px | --text-heading |
| heading-lg | 40px | 1.2 | -1px | --text-heading-lg |
| display | 48px | 1.15 | -1.2px | --text-display |

## Tokens — Spacing & Shapes

Base unit: 4px

Density: comfortable

### Spacing Scale

| Name | Value | Token |
|------|-------|-------|
| 4 | 4px | --spacing-4 |
| 8 | 8px | --spacing-8 |
| 12 | 12px | --spacing-12 |
| 16 | 16px | --spacing-16 |
| 20 | 20px | --spacing-20 |
| 24 | 24px | --spacing-24 |
| 32 | 32px | --spacing-32 |
| 40 | 40px | --spacing-40 |
| 48 | 48px | --spacing-48 |
| 56 | 56px | --spacing-56 |
| 60 | 60px | --spacing-60 |
| 64 | 64px | --spacing-64 |
| 80 | 80px | --spacing-80 |
| 84 | 84px | --spacing-84 |
| 96 | 96px | --spacing-96 |
| 100 | 100px | --spacing-100 |

### Border Radius

| Element | Value |
|---------|-------|
| cards | 16px |
| pills | 800px |
| buttons | 24px |
| default | 8px |
| largeButtons | 32px |

### Shadows

| Name | Value | Token |
|------|-------|-------|
| subtle | rgba(65, 61, 69, 0.2) 0px 2px 0px 0px | --shadow-subtle |

## Components

### Primary Action Button
Role: CTA

Filled button with 'Sky Connect' background (#0061ef), 'Pure White' text, and a 32px border-radius. Padding 14px vertical, 20px horizontal. Features a subtle shadow for soft depth.

### Ghost Button
Role: Secondary Action

Outlined button with 'Cloud Whisper' background (#f9f4f2), 'Charcoal Tone' text (#2d2c2b), and a 24px border-radius. Padding 0px vertical, 24px horizontal. Border 1px solid Charcoal Tone.

### Tab Button
Role: Navigation/Filter

Button with 'Pure White' background (#ffffff), 'Inkwell Gray' text (#4b4c4d), and an 8px border-radius. Padding 8px vertical, 16px-24px horizontal. Border 1px solid Pale Ash (#e2ded9).

### Dark Square Button
Role: Iconic/Informative

Square-shaped button with 'Charcoal Tone' background (#2d2c2b) and 'Pure White' text, likely for icons. Features a large (800px equivalent) border-radius making it circular, and 0px padding. Used for distinctive, usually smaller, interactive elements.

### Email Subscription Input
Role: Form Entry

Input field with 'Pure White' background (#ffffff), 'True Black' text (#000000), and an 8px border-radius. Padding 24px top, 8px bottom, 16px horizontal. Border 1px solid Light Stone (#d0d0d0).

### Content Card
Role: Information display

Container with 'Pure White' background (#ffffff), 28px border-radius, rgba(65, 61, 69, 0.2) 0px 2px 0px 0px shadow, and 16px-24px padding. Used for grouping related content.

### Accent Banner
Role: Promotional strip

Full-width bar with a 'Sunshine Burst' (#ffce00) background, containing a 'Charcoal Tone' text link. Used at the very top of the page for prominent announcements.

### Feature Pill Button
Role: Categorization/Navigation

Pill-shaped button with 'Charcoal Tone' background (#44423f) for icons/text like 'AI guidance', with 'Pure White' text. Has 800px border-radius (pill shape), and specific padding varying by content.

## Do's and Don'ts

### Do
- Prioritize 'Sky Connect' (#0061ef) for all primary call-to-action buttons and active navigation states.
- Apply 'Cloud Whisper' (#f9f4f2) for most large section backgrounds to maintain a soft, inviting atmosphere.
- Use border-radius 24px for general buttons and 32px for prominent CTA buttons to reinforce the soft, friendly aesthetic.
- Utilize 'Inkwell Gray' (#4b4c4d) as the primary text color for body copy and headings for optimal readability on light backgrounds.
- Ensure headings and body text use the Headspace Apercu font with careful application of letter-spacing adjustments.
- Incorporate the subtle shadow on buttons and cards to provide soft visual lift without heavy contrast.
- Use 24px and 16px as primary element gap values for consistent spacing between UI elements.

### Don't
- Avoid harsh, high-contrast shadows or sharp corners, as they contradict the brand's soft and approachable aesthetic.
- Do not use highly saturated colors for large text blocks; reserve them for accents, illustrations, and interactive elements.
- Refrain from using excessively small or tight letter-spacing for body text; the system clearly favors open and legible typography.
- Do not introduce new typefaces; stick to Headspace Apercu and its defined weights.
- Avoid full-bleed imagery without defined edges or masking; prefer contained, rounded elements or abstract backgrounds.
- Do not use dark backgrounds for entire sections, except where explicitly indicated for specific brand moments.
- Limit the use of 'True Black' (#000000) to critical input text or select emphasis, defaulting to 'Inkwell Gray' (#4b4c4d) for most text.

## Layout

The site employs a max-width centered layout for most content, providing generous white space around elements, contributing to a calm and focused experience. The hero section often features a centered headline over a 'Cloud Whisper' background, sometimes with a full-width accent banner at the very top. Content sections predominantly alternate light backgrounds with white card elements, or feature large content blocks with a Cloud Whisper or Pure White background. A distinct pattern of 2-column text+image sections is observed, with some feature sections using a loose grid of tab-like buttons. Navigation is a consistent sticky top-bar, and the footer is information-rich with a multi-column layout.

## Quick Color Reference
- Text (Inkwell Gray): #4b4c4d
- Background (Cloud Whisper): #f9f4f2
- CTA (Sky Connect): #0061ef
- Border (Pale Ash): #e2ded9
- Accent (Sunshine Burst): #ffce00
