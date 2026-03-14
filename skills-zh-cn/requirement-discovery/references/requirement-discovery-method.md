# Requirement Discovery Method

This reference expands the `requirement-discovery` skill into a reusable discussion framework for project and product leaders.

## What This Skill Adds Beyond Intent Recognition

Intent recognition answers:

- what the speaker seems to want right now

Requirement discovery answers:

- what problem is actually worth solving
- whether the idea has value
- which stakeholders matter
- what should happen next

Intent recognition is a lower layer. Requirement discovery is the management layer built on top of it.

## Four Capability Modules

### 1. Signal Recognition

Recognize:

- explicit requests
- hidden concerns
- emotional urgency
- stakeholder position
- maturity of the demand

### 2. Clarification Dialogue

Drive multi-round discussion to reduce ambiguity.

Useful question buckets:

- object: 谁受影响
- scenario: 在什么场景下发生
- pain: 现在的问题是什么
- value: 为什么值得做
- timing: 为什么现在做
- ownership: 谁负责推动

### 3. Value Assessment

Test the demand on these dimensions:

- frequency
- impact
- urgency
- strategic fit
- evidence strength
- execution cost

Suggested judgment:

- `go`: value and timing are clear
- `test`: value is plausible but evidence is insufficient
- `hold`: problem exists but timing or ownership is weak
- `no-go`: low value or false problem

### 4. Requirement Consolidation

Turn discussion into a stable artifact:

- concise requirement statement
- target users
- problem statement
- expected value
- scope boundary
- open issues
- next action

## Stage-Based Prompting

### Early Stage

Use when the input is only a thought, complaint, or vague task.

Prompt pattern:

- summarize the current idea in one sentence
- identify what is known and unknown
- ask the single next best clarification question

### Middle Stage

Use when the problem exists but value or scope is still fuzzy.

Prompt pattern:

- restate the working problem
- test value and urgency
- identify minimum scope and non-goals

### Late Stage

Use when stakeholders need something actionable.

Prompt pattern:

- produce a requirement brief
- list unresolved risks
- recommend the next owner and next meeting goal

## Output Template

Use this when the conversation is mature enough:

```text
需求名称：

一、背景
这件事为什么被提出来？

二、目标用户
谁会直接受到影响？

三、核心问题
现在具体哪里不好？

四、预期价值
解决后能带来什么变化？

五、建议范围
这一轮先做什么，不做什么？

六、成功标准
什么结果可以说明这件事有效？

七、待确认问题
还有哪些问题没说清楚？

八、下一步建议
建议继续调研、设计验证、小范围试点，还是直接立项？
```

## Anti-Patterns

Watch for these common mistakes:

- confusing stakeholder opinion with user evidence
- discussing screens before confirming value
- treating urgency as proof of importance
- expanding scope because no one defines non-goals
- writing a fake-complete requirement while key questions remain unanswered
