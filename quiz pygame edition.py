import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the screen
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Quiz Game")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Fonts
font = pygame.font.Font(None, 36)

# Questions and answers
questions = [
    "What is the capital of France?",
    "Which continent is the largest by land area?",
    "What is the longest river in the world?",
    "Which country is famous for kangaroos and koalas?"
]

answers = [
    ["Rome", "Paris", "Berlin", "London"],
    ["North America", "Africa", "Europe", "Asia"],
    ["Nile", "Amazon", "Yangtze", "Mississippi"],
    ["India", "Canada", "Brazil", "Australia"]
]

correct_answers = [1, 3, 0, 3]  # Index of the correct answer for each question

# Function to display popup message
def display_popup(message, color):
    popup_text = font.render(message, True, color)
    popup_rect = popup_text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
    pygame.draw.rect(screen, WHITE, popup_rect.inflate(20, 20))
    screen.blit(popup_text, popup_rect)
    pygame.display.flip()
    pygame.time.delay(1500)  # Delay for 1.5 seconds

# Main loop
def quiz_game():
    global score  # Declare score as global
    score = 0
    question_index = 0

    running = True
    while running:
        screen.fill(WHITE)
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # Left mouse button clicked
                    # Check if an answer is clicked
                    question_index = check_answer_at(event.pos, question_index)

        # Display question
        display_question(question_index)
        display_answers(question_index)

        pygame.display.flip()

# Function to display question
def display_question(index):
    question_text = font.render(questions[index], True, BLACK)
    screen.blit(question_text, (50, 50))

# Function to display answer choices
def display_answers(index):
    choices = answers[index]
    y_offset = 100
    for i, choice in enumerate(choices):
        choice_text = font.render(f"{i+1}. {choice}", True, BLACK)
        screen.blit(choice_text, (50, y_offset))
        y_offset += 50

# Function to check the answer
def check_answer_at(pos, question_index):
    global score
    x, y = pos
    # Check if the click is within the bounds of the answer choices
    if 50 <= x <= 250:
        choice = (y - 100) // 50  # Calculate which answer is clicked based on y-coordinate
        if 0 <= choice < len(answers[question_index]):
            if choice == correct_answers[question_index]:
                display_popup("Correct!", GREEN)
                score += 1
            else:
                display_popup("Incorrect!", RED)
            question_index += 1

            if question_index >= len(questions):
                # Display final score
                display_popup(f"Quiz completed! Your score: {score}/{len(questions)}", BLACK)
                pygame.quit()
                sys.exit()
    
    return question_index

# Start the game
quiz_game()
