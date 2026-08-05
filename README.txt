FONO

Project overview for designers, linguists, educators, creators, and planning conversations with an LLM.

What this project is

Fono is a small browser-based listening and transcription experience built around a custom phonetic symbol board. A learner hears an audio clip, reconstructs the sequence by selecting symbols on the board, and receives immediate feedback on whether the answer is correct.

The current project is best understood as a playable prototype for phonological perception, symbol familiarization, and sequence recall. It is not yet a full curriculum, assessment platform, or content management system. Its value today is that it makes the core interaction tangible: hear a sound pattern, map it onto a visual phonetic system, and observe what learners can and cannot recover.

Why it matters

This project sits at the intersection of several goals:

Linguistic representation
It proposes a compact symbol set and a spatial arrangement that suggests relationships among sounds.

Learning design
It turns phonetic listening into an active task rather than passive exposure.

Creative system building
It treats sound, notation, interface layout, and feedback as parts of one designed experience.

Research potential
It already captures simple performance data that could become the basis for error analysis, curriculum planning, or adaptive sequencing.

What the learner currently experiences

1. The learner opens a single-page interface containing a field of phonetic symbols.
2. The learner requests a new sound.
3. The app plays one audio clip selected from the current library.
4. The learner reconstructs the sound sequence by clicking symbols or using the keyboard.
5. The learner submits the guess.
6. The app responds with a binary result: correct or incorrect.
7. The learner can replay the clip and try again with another item.

This makes the current experience fast, game-like, and low-friction. The interaction is simple enough to test with participants immediately, but it is also minimal enough that many design and pedagogical opportunities remain open.

What is in the content library now

The repository currently includes three sets of audio material organized by sequence length:

2-fonz
Short two-symbol items.
Current size: 40 clips.

3-fonz
Three-symbol items.
Current size: 170 clips.

5-fonz
Five-symbol items.
Current size: 200 clips.

Total indexed clips in the current app database: 410.

This structure suggests a progression from simpler to more complex listening tasks, even though the present interface does not yet expose that progression as an explicit learning path.

What the symbol board seems to be doing

The interface arranges a fixed inventory of symbols on a two-dimensional field, with connecting lines between some of them and small secondary dots attached to others. The arrangement appears to communicate a designed phonological space rather than an arbitrary button grid.

Even without a written legend, the board conveys several ideas:

1. Some sounds belong to visible families or neighborhoods.
2. Some sounds are variants or marked forms of others.
3. The learner is meant to navigate a system, not just identify isolated items.

For a linguist or educator, this is one of the project's most distinctive qualities. The interface is already an argument about how the sound system should be seen, not just heard.

What the app currently remembers

The app stores the correct sequence for each audio clip and keeps basic per-symbol guess statistics.

At the moment, the recorded feedback is simple:

1. Which symbol sequence was expected.
2. Whether the learner's submission was correct.
3. Aggregate counts of how often each symbol appears in correct versus total guesses.

This is enough to support early questions such as:

1. Which symbols are persistently difficult?
2. Which sequences produce the most confusion?
3. Does difficulty rise mainly with sequence length, with certain symbol contrasts, or with particular positions inside a sequence?

What the project is not yet doing

The current prototype does not yet provide:

1. Learner profiles or progress histories.
2. Session-level analytics.
3. Fine-grained error analysis beyond correct or incorrect outcomes.
4. Explanations, hints, or teaching interventions after an error.
5. Guided lessons, levels, or curricular sequencing.
6. Multiple display modes for different audiences such as novices, experts, children, or researchers.
7. Editorial tools for managing or extending the audio library from within the interface.

This is useful to state plainly because the next phase of the project is less about repairing a broken idea and more about deciding what kind of product or research instrument it should become.

How to think about Fono as an experience design project

Fono is not only a quiz. It is a designed encounter between ear, symbol, memory, and classification.

From an experience design perspective, the important questions are:

1. What emotional tone should the act of listening and guessing have: playful, scholarly, meditative, competitive, exploratory?
2. Should the symbol field feel like a map, a keyboard, a constellation, a lab instrument, or a game board?
3. When a learner fails, should the system merely judge, or should it reveal structure?
4. What kind of reward matters here: correctness, insight, speed, pattern recognition, or self-awareness of contrast?

The current prototype already supports a strong "map of sounds" metaphor. A next design step could deepen that metaphor instead of flattening the experience into a conventional flashcard workflow.

How to think about Fono as a linguistic project

For a linguist, the most important question is whether the symbol inventory, spatial layout, and audio sets together form a coherent descriptive system.

Useful lines of inquiry include:

1. What exact phonological or pedagogical theory is the board encoding?
2. Are the symbols intended as IPA, a modified IPA, or a project-specific notation?
3. Which contrasts are central to the learning goal?
4. Does spatial proximity correspond to articulatory similarity, acoustic similarity, teaching convenience, or another logic?
5. Are the audio items nonce forms, minimal-contrast exercises, lexical materials, or something in between?

Documenting those choices would help both human collaborators and LLM agents reason about future directions more productively.

How to think about Fono as an educational tool

Pedagogically, the prototype currently emphasizes recall and discrimination. It asks the learner to convert heard sequences into symbolic sequences without much scaffolding.

That creates several possible futures:

1. Foundational training tool
Focus on symbol recognition, familiarization, and basic sound discrimination.

2. Assessment instrument
Use the app to identify which contrasts or sequence patterns are hardest for specific learners or cohorts.

3. Creative learning environment
Let learners compose, compare, or manipulate sound sequences rather than only decode them.

4. Research probe
Use controlled item sets to study perceptual confusions, representational bias, or the effect of interface layout on phonological learning.

Each path would produce a different roadmap, different metrics, and different content needs.

How to think about Fono as a management and strategy project

At a planning level, Fono appears to be at the stage where conceptual clarity matters more than feature volume. The main management task is to decide which role the project should play in the next iteration.

The key strategic choices are:

1. Audience
Who is this for first: linguists, students, children, second-language learners, speech professionals, curious creators?

2. Outcome
What should improve through use: transcription skill, sound awareness, theoretical understanding, confidence, speed, or data collection?

3. Mode
Is this primarily a teaching tool, a demonstration artifact, a research instrument, or a public interactive experience?

4. Scope
Should the next phase deepen one tightly defined learning journey or broaden the platform into a more flexible sound-learning environment?

Without these decisions, new features risk becoming scattered. With them, the existing prototype becomes a strong foundation rather than a partial product.

Promising directions for next-step brainstorming

1. Make the hidden structure legible
Add a legend, grouping cues, or reveal-on-demand explanations so learners understand what the map of symbols is trying to teach.

2. Turn content tiers into explicit pathways
Present 2-fonz, 3-fonz, and 5-fonz as stages, challenges, or modules rather than only as background inventory.

3. Move beyond binary feedback
Show where a guess diverged from the target, which positions were right, and which sound families are commonly confused.

4. Capture richer learning data
Track attempts, retries, response time, and confusion patterns in ways that support both pedagogy and research.

5. Add teaching modes
Include listen-first, see-then-hear, contrast pairs, guided practice, and free exploration.

6. Support multiple audiences
Offer alternate interface framings for novice learners, expert linguists, children, or workshop participants.

7. Clarify the notation system
Write down what each symbol means, where it comes from, and why the board is arranged as it is.

8. Build a content-authoring story
Make it easier to add new audio sets, annotate them, group them, and describe their pedagogical purpose.

9. Introduce narrative or creative framing
The current interaction could become more memorable if framed as exploration, listening missions, sound archaeology, or composition.

10. Use the data diagnostically
Convert aggregate success rates into maps of difficulty that help refine the board, the content, or the pedagogy.

Questions an LLM collaborator could help explore next

1. What learning theories best match the current interaction model?
2. What alternative spatial layouts could better express the sound relationships?
3. What terminology should the project use for nontechnical audiences?
4. How might the app explain its notation system without overwhelming the learner?
5. What forms of feedback would make errors more educational?
6. How could the current audio inventory be reorganized into lessons, games, or research protocols?
7. What analytics would be most meaningful for a linguist versus a teacher versus a product manager?
8. What version of this product would be compelling in a classroom, a museum, a workshop, or an online course?

Current technical shape, stated briefly

The project is currently a lightweight web app with one main interface, an audio library, and a small local database for storing answer keys and guess counts. This matters mainly because it means the concept is already concrete and testable. It is not just an idea sketch.

In practical terms, the prototype is ready for conceptual refinement: clearer theory, clearer audience, clearer pedagogy, and clearer experience direction.

Bottom line

Fono already contains a meaningful core idea: sound sequences can be learned through an explorable visual phonetic system rather than through plain text transcription drills alone.

The next phase should focus on defining what kind of experience this wants to become. The strongest opportunities are not merely technical additions, but sharper articulation of the notation, the learning model, the audience, and the role of feedback.

If those foundations are clarified, the current prototype can evolve into a distinctive tool for phonological learning, creative exploration, or linguistic research.