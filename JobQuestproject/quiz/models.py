from django.db import models

class Topic(models.Model):
    title = models.CharField(max_length=255,null=True)
    def __str__(self):
        return self.title

class Question(models.Model):
    topic = models.ForeignKey(Topic, related_name='questions', on_delete=models.CASCADE,null=True)
    text = models.CharField(max_length=255,null=True)
    def __str__(self):
        return self.text

class Answer(models.Model):
    question = models.ForeignKey(Question, related_name='answers', on_delete=models.CASCADE,null=True)
    text = models.CharField(max_length=255,null=True)
    option_letter = models.CharField(max_length=1, choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D')],null=True)
    is_correct = models.BooleanField(default=False,null=True)

    def __str__(self):
        return self.text