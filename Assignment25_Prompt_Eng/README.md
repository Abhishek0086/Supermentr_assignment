# Assignment 25: Prompt Engineering

## Overview
A comprehensive guide to prompt engineering that demonstrates how to write effective prompts for AI models by comparing weak vs. strong prompts across different use cases.

## What is Prompt Engineering?
Prompt engineering is the process of designing effective inputs (prompts) to get accurate and useful responses from AI models. A well-structured prompt gives better results than a vague one.

## Objective
To compare weak and strong prompts and understand how prompt design affects AI output quality, relevance, and usefulness.

## Prompt Comparisons

### A. Resume Generation

#### Weak Prompt
```
"Make my resume"
```

**Problems:**
- Too vague and unclear
- No details about the person
- No format specifications
- No context about experience level
- Ambiguous output expectations

**Output Quality**: Generic, likely missing important details

---

#### Strong Prompt
```
"Create a professional resume for a 3rd-year Computer Science student skilled in Python, JavaScript, React, and AWS. Include projects, skills, and internship experience in a clean format."
```

**Improvements:**
- Clear role and experience level
- Specific technical skills listed
- Defined sections to include
- Format specification
- Context about education

**Output Quality**: Targeted, detailed, and well-structured

---

### B. Business Idea

#### Weak Prompt
```
"Give me a business idea"
```

**Problems:**
- No domain or industry specified
- No target audience
- No constraints or requirements
- Generic output likely
- No scalability considerations

**Output Quality**: Generic, may not be actionable

---

#### Strong Prompt
```
"Suggest a unique startup idea in the food industry targeting college students in India, focusing on low cost and high scalability. Include revenue model and competitive advantage."
```

**Improvements:**
- Target audience clearly defined
- Domain specified (food industry)
- Geographic focus (India)
- Constraints included (low cost, high scalability)
- Additional requirements (revenue model, competitive advantage)

**Output Quality**: Specific, actionable, and tailored

---

### C. Study Plan

#### Weak Prompt
```
"Make a study plan"
```

**Problems:**
- No subject or topic specified
- No timeline or duration
- No skill level mentioned
- No learning objectives
- Ambiguous structure

**Output Quality**: Generic, may not match needs

---

#### Strong Prompt
```
"Create a 30-day study plan for learning Python and cloud computing for a beginner, including daily topics, practice tasks, and milestones. Format as a week-by-week breakdown."
```

**Improvements:**
- Time-bound (30 days)
- Subjects clearly defined
- Skill level specified (beginner)
- Structured output requested
- Specific components included (daily topics, practice tasks, milestones)
- Format specification (week-by-week)

**Output Quality**: Structured, actionable, and tailored to skill level

---

## Key Differences Between Weak and Strong Prompts

| Aspect | Weak Prompt | Strong Prompt |
|--------|------------|---------------|
| Clarity | Vague and unclear | Specific and detailed |
| Context | Missing | Comprehensive |
| Constraints | None | Well-defined |
| Goals | Ambiguous | Clear objectives |
| Format | Not specified | Explicitly stated |
| Audience | Not considered | Clearly defined |
| Detail Level | Minimal | Comprehensive |
| Output Quality | Generic | Targeted |

---

## Prompt Engineering Best Practices

### 1. Be Specific
- Include relevant details
- Avoid vague language
- Define scope clearly

### 2. Provide Context
- Explain the background
- Mention constraints
- Specify use case

### 3. Define Output Format
- Specify structure (bullet points, paragraphs, etc.)
- Mention length requirements
- Request specific sections

### 4. Include Examples
- Provide sample outputs
- Show desired style
- Clarify expectations

### 5. Set Constraints
- Budget or cost limits
- Time constraints
- Audience level
- Technical requirements

### 6. Ask for Reasoning
- Request explanations
- Ask for step-by-step breakdown
- Request justification

### 7. Iterate and Refine
- Test different phrasings
- Adjust based on results
- Refine for better outputs

---

## Prompt Engineering Techniques

### 1. Few-Shot Learning
Provide examples of desired output:
```
"Generate 3 more business ideas similar to these:
1. [Example 1]
2. [Example 2]"
```

### 2. Role-Based Prompting
Assign a role to the AI:
```
"You are an experienced resume writer. Create a resume for..."
```

### 3. Chain-of-Thought
Ask for step-by-step reasoning:
```
"Explain your reasoning step-by-step as you create the study plan."
```

### 4. Constraint-Based
Add specific limitations:
```
"Create a business idea with a budget of $5000 and 3-month timeline."
```

### 5. Structured Output
Request specific format:
```
"Format the output as:
- Title
- Description
- Implementation Steps
- Expected Outcomes"
```

---

## Real-World Applications

### Content Creation
- Blog posts and articles
- Social media content
- Marketing copy

### Code Generation
- Function implementations
- Bug fixes
- Code refactoring

### Business Planning
- Business plans
- Market analysis
- Strategy documents

### Education
- Study materials
- Lesson plans
- Practice questions

### Customer Service
- Response templates
- FAQ generation
- Support documentation

---

## Common Mistakes to Avoid

### 1. Being Too Vague
❌ "Write something about AI"
✅ "Write a 500-word article about AI applications in healthcare"

### 2. Unclear Expectations
❌ "Make it good"
✅ "Make it professional, concise, and suitable for a job interview"

### 3. Missing Context
❌ "Create a plan"
✅ "Create a 12-week project plan for a web development team of 5 people"

### 4. No Format Specification
❌ "List ideas"
✅ "List 5 ideas in bullet points with brief descriptions"

### 5. Ambiguous Scope
❌ "Tell me about Python"
✅ "Explain Python's key features for beginners in 200 words"

---

## Measuring Prompt Quality

### Factors to Consider:
1. **Relevance**: Does output match the request?
2. **Accuracy**: Is the information correct?
3. **Completeness**: Are all aspects covered?
4. **Clarity**: Is the output easy to understand?
5. **Actionability**: Can the output be used immediately?
6. **Efficiency**: Was the prompt concise?

---

## Concepts Covered
- Prompt design principles
- AI model behavior
- Input-output relationships
- Communication with AI
- Optimization techniques
- Best practices for AI interaction

## Conclusion
Prompt engineering plays a crucial role in getting accurate and useful results from AI systems. Well-designed prompts:
- Improve output quality
- Save time and iterations
- Reduce ambiguity
- Increase relevance
- Enhance efficiency

By understanding the principles of prompt engineering and practicing with different approaches, you can significantly improve your interactions with AI models and get better results for your specific needs.

## Practice Exercise
Try rewriting these weak prompts into strong ones:
1. "Write about climate change"
2. "Create a marketing plan"
3. "Explain machine learning"
4. "Design a website"
5. "Write a story"

Compare your strong prompts with others and test them with an AI model to see the difference in output quality!
