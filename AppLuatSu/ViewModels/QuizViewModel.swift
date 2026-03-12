import Foundation
import SwiftUI

class QuizViewModel: ObservableObject {
    @Published var questions: [Question] = []
    @Published var currentQuestionIndex = 0
    @Published var selectedAnswer: String? = nil
    @Published var score = 0
    @Published var showExplanation = false
    @Published var isFinished = false
    
    var currentQuestion: Question? {
        guard currentQuestionIndex < questions.count else { return nil }
        return questions[currentQuestionIndex]
    }
    
    init() {
        loadQuestions()
    }
    
    func loadQuestions() {
        // Trên iOS, bạn sẽ cần file questions.json trong Bundle
        guard let url = Bundle.main.url(forResource: "questions", withExtension: "json") else {
            print("Không tìm thấy file questions.json")
            return
        }
        
        do {
            let data = try Data(contentsOf: url)
            let decoder = JSONDecoder()
            self.questions = try decoder.decode([Question].self, from: data)
            // Có thể xáo trộn câu hỏi nếu muốn
            // self.questions.shuffle()
        } catch {
            print("Lỗi khi load dữ liệu: \(error)")
        }
    }
    
    func selectAnswer(_ key: String) {
        if selectedAnswer == nil {
            selectedAnswer = key
            if key == currentQuestion?.answer {
                score += 1
            }
            showExplanation = true
        }
    }
    
    func nextQuestion() {
        if currentQuestionIndex + 1 < questions.count {
            currentQuestionIndex += 1
            selectedAnswer = nil
            showExplanation = false
        } else {
            isFinished = true
        }
    }
    
    func resetQuiz() {
        currentQuestionIndex = 0
        selectedAnswer = nil
        score = 0
        showExplanation = false
        isFinished = false
        questions.shuffle()
    }
}
