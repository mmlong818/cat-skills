# Skillforge Method

Source inspiration: [mmlong818/skillforge](https://github.com/mmlong818/skillforge/tree/skills/skill)

This reference captures the useful core of that approach in Codex-friendly terms.

## What It Tries To Solve

Many skills fail because they are:

- too vague to trigger
- too long to read
- too generic to guide action
- too tied to one repository or tool

The method fixes that by forcing the creator to move from real examples to a compact reusable workflow.

## Seven-Step Method

### 1. Name the repeated job

Describe the repeated job in one sentence. If the sentence sounds broad, narrow it.

### 2. Gather examples

List real user requests that should trigger the skill. Use them as design tests.

### 3. Find the reusable pieces

For each example, ask:

- what instructions repeat every time
- what code should become a script
- what bulky details should become references
- what files should become assets

### 4. Build only the necessary structure

Keep the root simple:

- `SKILL.md`
- optional `scripts/`
- optional `references/`
- optional `assets/`
- optional `agents/openai.yaml`

### 5. Write the trigger first

A strong description should answer:

- what the skill does
- when it should be used
- which tasks, file types, or scenarios should trigger it

### 6. Write operational instructions

Tell the next agent exactly how to work:

- first read
- decision points
- checks
- success criteria

### 7. Use and refine

The first real use reveals what is missing. Improve the skill after actual execution, not only from theory.

## Practical Prompt Shape

When using this method, the request can be framed like:

- create a skill for this repeated task
- turn this workflow into a reusable Codex skill
- adapt this external skill into a Codex-native version
- review this existing skill and make it trigger more reliably

## Good Signs

A skill made with this method usually has:

- a crisp description
- short, direct instructions
- limited but useful resources
- clear validation guidance

## Bad Signs

The skill likely needs rework if it contains:

- marketing language
- long theory sections
- many files with little execution value
- trigger conditions hidden in the body
- copied external assumptions that do not match Codex
