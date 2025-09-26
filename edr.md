# Entity-Relationship Diagram (ERD) for Poll Project API's

This ERD illustrates the data models and their relationships within the Poll Project, specifically focusing on the `pollApp` which exposes the core API functionality.

```
+------------------+       +------------------+
|     Question     |       |      Choice      |
+------------------+       +------------------+
| id (PK)          |<----- | id (PK)          |
| question_text    |       | question (FK)    |
| pub_date         |       | choice_text      |
+------------------+       | votes            |
                           +------------------+
```

## Explanation of Entities:

### Question
Represents a poll question.

*   **`id`**: (Primary Key) A unique identifier for each question.
*   **`question_text`**: The actual text of the poll question.
*   **`pub_date`**: The date and time when the question was published.

### Choice
Represents a possible answer choice for a poll question.

*   **`id`**: (Primary Key) A unique identifier for each choice.
*   **`question`**: (Foreign Key) Links a choice to its corresponding question. This establishes a one-to-many relationship, meaning one `Question` can have multiple `Choice`s.
*   **`choice_text`**: The text of the answer choice.
*   **`votes`**: An integer field to store the number of votes received for this choice.

## Relationships:

*   **One-to-Many (Question to Choice)**:
    *   A `Question` can have multiple `Choice`s.
    *   Each `Choice` belongs to exactly one `Question`.
    *   Represented by the `question (FK)` field in the `Choice` entity, referencing the `id` of the `Question` entity.
