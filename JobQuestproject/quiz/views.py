from django.shortcuts import render, redirect,get_object_or_404
from django.contrib import messages
from .models import Topic, Question, Answer

def quiz_list(request):
    topics = Topic.objects.all()
    return render(request, 'quiz/quiz_list.html', {'topics': topics})

def quiz_detail(request, topic_id):
    topic = Topic.objects.get(id=topic_id)
    questions = topic.questions.all()
    return render(request, 'quiz/quiz_detail.html', {'topic': topic, 'questions': questions})

def quiz_result(request, topic_id):
    if request.method == 'POST':
        topic = get_object_or_404(Topic, id=topic_id)
        questions = topic.questions.all()
        total_questions = questions.count()
        score = 0
        
        for question in questions:
            # Retrieve the selected answer from POST data
            selected_answer_id = request.POST.get(f'question_{question.id}')
            
            # Get correct answer for the question
            correct_answer = question.answers.get(is_correct=True)
            
            # Check if the selected answer is correct
            if selected_answer_id:
                selected_answer = Answer.objects.get(id=int(selected_answer_id))
                if selected_answer.is_correct:
                    score += 1
        
        # Calculate percentage score
        if total_questions > 0:
            percentage_score = (score / total_questions) * 100
        else:
            percentage_score = 0
        
        # Prepare context to pass to template
        context = {
            'topic': topic,
            'total_questions': total_questions,
            'score': score,
            'percentage_score': percentage_score,
        }
        
        return render(request, 'quiz/quiz_result.html', context)
    else:
        # If GET request or any other method, redirect to quiz list
        messages.error(request, 'Invalid request. Please submit the quiz form.')
        return redirect('quiz_list')