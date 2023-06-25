Project Aleksandria
===================

Simple project to reqister users on courses.

```mermaid
classDiagram
    Course --|> User : author
    Enrollment --|> User
    Enrollment --|> Course
    Review --|> User : user
    Review --|> Course : course

```

