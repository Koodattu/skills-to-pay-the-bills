---
name: end-user-ui-ux
description: >
  Use when designing, implementing, redesigning, or auditing desktop web,
  mobile web, or native mobile interfaces for real end users. Optimize task
  success, comprehension, recovery, platform fit, accessibility, responsive
  or adaptive behavior, and coherent product-specific visual design.
---

# End-User UI/UX

## Priorities

Optimize in this order:

1. User task success and comprehension.
2. Prevention, recognition, and recovery from errors.
3. Platform conventions, accessibility, and input ergonomics.
4. Information hierarchy and complete product states.
5. Coherent, product-specific visual identity.
6. Delight where it does not slow or obscure the task.

Do not use visual novelty to compensate for a weak workflow.

## Classify the work

Before acting, classify:

- Surface:
  - marketing or brand;
  - product or operational;
  - native mobile.
- Scope:
  - greenfield;
  - substantial redesign;
  - scoped change.
- Primary environment:
  - desktop keyboard and mouse;
  - mobile touch;
  - tablet;
  - mixed.

Do not apply landing-page composition to operational product UI.

Operational interfaces should generally prioritize scanning, comparison,
predictable navigation, repeated actions, clear state, and restrained chrome.

Native applications must respect platform navigation, back behavior, safe
areas, system sheets, permissions, keyboards, text scaling, and accessibility
semantics.

## Read product context

Read, when present:

- `PRODUCT.md`
- `UX.md`
- `DESIGN.md`
- `UI_ACCEPTANCE.md`
- `DECISIONS.md`
- existing design tokens and components
- adjacent screens and flows

For non-trivial greenfield work, create concise drafts of missing product
documents before implementation.

For scoped work, infer from the existing product and do not introduce an
unrelated redesign.

Identify:

- target user;
- primary job;
- frequency and context of use;
- user expertise;
- urgency and cost of failure;
- critical flow;
- business constraints;
- non-goals;
- canonical components and tokens.

State only material assumptions. Prefer reversible defaults. Do not invent an
elaborate fictional persona.

## Use references precisely

Treat screenshots and Figma frames as evidence, not vague inspiration.

For each reference, record:

- what to borrow;
- what not to borrow;
- whether the relevant quality is hierarchy, density, navigation,
  composition, typography, interaction, motion, or tone.

Use anti-references to name rejected patterns.

Use realistic domain content and realistic data shapes. Avoid lorem ipsum and
generic placeholder dashboards where real content can be inferred.

## Before implementation

Produce a concise design read containing:

- user, job, and context;
- information hierarchy;
- primary interaction model;
- visual thesis;
- critical assumptions;
- acceptance scenarios.

Map:

- primary flow;
- entry and exit;
- navigation and back behavior;
- default, loading, empty, partial, success, error and validation states;
- permissions and offline behavior where applicable;
- destructive actions and recovery;
- desktop, mobile and tablet adaptations.

For greenfield or substantial redesign work:

1. Generate two or three low-fidelity structural directions.
2. Compare them against user-task, platform, accessibility and implementation
   criteria.
3. Select one.
4. Record the selection and rejected alternatives in `DECISIONS.md`.
5. Implement only the selected direction.

For scoped work, preserve the existing direction.

## Visual-direction rules

Use exactly one primary aesthetic-direction skill during a design pass.
Audit and testing skills may be used in addition.

Reuse the existing token and component system. Do not create a parallel
design system in an established repository.

Prefer semantic controls that match the user task.

Use typography, spacing, alignment, contrast, content order, grouping and
progressive disclosure before adding decoration.

Cards are appropriate for independently framed objects or interactions.
Do not use cards as the default wrapper for every section.

Avoid unless justified by the product:

- nested cards;
- generic gradient blobs;
- repeated rounded icon tiles;
- excessive pills;
- arbitrary oversized headings;
- low-contrast gray text;
- decorative glass effects;
- marketing copy in operational screens;
- animation on frequent keyboard-driven operations.

Motion must explain state, preserve spatial continuity, or provide useful
feedback. Otherwise omit it.

Responsive design must fit the available space. Adaptive design must keep the
interaction model usable in that space. Do not merely shrink a desktop layout
onto mobile.

## Implementation

Implement the smallest complete vertical slice of the highest-value user
task.

Reuse existing:

- architecture;
- routing;
- state management;
- data access;
- tokens;
- components;
- validation;
- error handling.

Do not build a landing page when the request is for an application.

Add accessibility while implementing:

- semantic controls;
- names and labels;
- focus order;
- keyboard behavior;
- touch targets;
- contrast;
- text scaling;
- reduced-motion behavior.

Do not defer accessibility to a final cleanup pass.

## Verification

Create a QA inventory from:

- task requirements;
- visible controls;
- state changes;
- navigation;
- accessibility requirements;
- claims made by the implementation.

Run functional and visual QA as separate passes.

### Web

Use the browser or Playwright.

Test:

- the critical flow with normal mouse, keyboard and touch input;
- every changed interactive control;
- desktop and mobile layouts;
- minimum supported viewport;
- densest realistic state;
- at least one post-interaction state;
- loading, empty, error and validation states;
- long and translated content;
- keyboard navigation;
- reduced motion.

Capture viewport screenshots.

Inspect:

- overflow and clipping;
- hierarchy;
- alignment;
- spacing;
- density;
- contrast;
- focus state;
- sticky and fixed elements;
- navigation behavior;
- transition behavior.

### Native mobile

Use `agent-device` or `mobile-mcp` or `browser skill` on a simulator, emulator, device, or expo web.

Test:

- cold launch and resumed launch;
- primary navigation;
- operating-system back behavior;
- keyboard appearance and dismissal;
- safe areas;
- system and permission sheets;
- denied permissions;
- loading, offline and error recovery;
- text scaling;
- rotation and tablet layouts where supported;
- accessibility semantics.

Convert stable critical flows into Maestro or platform integration tests.

### All platforms

Automated checks supplement rather than replace manual visual inspection and
target-user testing.

## Iteration

After each verification pass:

1. Rank findings by user impact.
2. Fix at most the top three coherent issues.
3. Freeze unaffected regions.
4. Re-test affected scenarios.
5. Record lasting decisions in `DECISIONS.md`.

Do not add decoration to solve an interaction or information problem.

Stop after the acceptance criteria pass.

Default maximum: three visual-refinement passes unless a named acceptance
criterion still fails.

## Completion report

Report:

- implemented user flow;
- major product and visual decisions;
- functional scenarios tested;
- visual scenarios inspected;
- screenshots, tests, or other evidence produced;
- known limitations or untested cases;
- decisions requiring validation with actual users.