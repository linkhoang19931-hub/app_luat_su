import SwiftUI

struct QuestionView: View {
    @StateObject var viewModel = QuizViewModel()
    
    var body: some View {
        NavigationView {
            VStack {
                if let question = viewModel.currentQuestion {
                    ScrollView {
                        VStack(alignment: .leading, spacing: 20) {
                            // Progress bar
                            ProgressView(value: Double(viewModel.currentQuestionIndex + 1), total: Double(viewModel.questions.count))
                                .accentColor(.blue)
                            
                            Text("Câu \(viewModel.currentQuestionIndex + 1) / \(viewModel.questions.count)")
                                .font(.subheadline)
                                .foregroundColor(.secondary)
                            
                            Text(question.question)
                                .font(.title3)
                                .fontWeight(.bold)
                                .padding(.vertical)
                            
                            ForEach(question.sortedOptions, id: \.key) { key, value in
                                OptionButton(
                                    key: key,
                                    value: value,
                                    isSelected: viewModel.selectedAnswer == key,
                                    isCorrect: question.answer == key,
                                    showResult: viewModel.selectedAnswer != nil,
                                    action: {
                                        viewModel.selectAnswer(key)
                                    }
                                )
                                .disabled(viewModel.selectedAnswer != nil)
                            }
                            
                            if viewModel.showExplanation {
                                ExplanationView(explanation: question.explanation)
                                    .transition(.move(edge: .bottom).combined(with: .opacity))
                            }
                        }
                        .padding()
                    }
                    
                    Spacer()
                    
                    if viewModel.selectedAnswer != nil {
                        Button(action: {
                            withAnimation {
                                viewModel.nextQuestion()
                            }
                        }) {
                            Text(viewModel.currentQuestionIndex + 1 < viewModel.questions.count ? "Tiếp theo" : "Xem kết quả")
                                .frame(maxWidth: .infinity)
                                .padding()
                                .background(Color.blue)
                                .foregroundColor(.white)
                                .cornerRadius(10)
                                .padding()
                        }
                    }
                } else if viewModel.isFinished {
                    ResultView(score: viewModel.score, total: viewModel.questions.count, action: viewModel.resetQuiz)
                } else {
                    Text("Đang tải dữ liệu...")
                }
            }
            .navigationTitle("Ôn Thi Luật Sư")
        }
    }
}

// Custom Button cho các lựa chọn
struct OptionButton: View {
    let key: String
    let value: String
    let isSelected: Bool
    let isCorrect: Bool
    let showResult: Bool
    let action: () -> Void
    
    var backgroundColor: Color {
        if !showResult {
            return isSelected ? .blue.opacity(0.1) : .clear
        }
        if isCorrect {
            return .green.opacity(0.2)
        }
        if isSelected && !isCorrect {
            return .red.opacity(0.2)
        }
        return .clear
    }
    
    var borderColor: Color {
        if !showResult {
            return isSelected ? .blue : Color.gray.opacity(0.3)
        }
        if isCorrect {
            return .green
        }
        if isSelected && !isCorrect {
            return .red
        }
        return Color.gray.opacity(0.3)
    }
    
    var body: some View {
        Button(action: action) {
            HStack {
                Text(key)
                    .fontWeight(.bold)
                    .frame(width: 30)
                
                Text(value)
                    .multilineTextAlignment(.leading)
                
                Spacer()
                
                if showResult {
                    if isCorrect {
                        Image(systemName: "checkmark.circle.fill").foregroundColor(.green)
                    } else if isSelected {
                        Image(systemName: "xmark.circle.fill").foregroundColor(.red)
                    }
                }
            }
            .padding()
            .background(backgroundColor)
            .cornerRadius(10)
            .overlay(
                RoundedRectangle(cornerRadius: 10)
                    .stroke(borderColor, lineWidth: 2)
            )
        }
        .foregroundColor(.primary)
    }
}

// View hiển thị giải thích
struct ExplanationView: View {
    let explanation: String
    
    var body: some View {
        VStack(alignment: .leading, spacing: 10) {
            HStack {
                Image(systemName: "lightbulb.fill")
                    .foregroundColor(.yellow)
                Text("Giải thích")
                    .font(.headline)
            }
            
            Text(explanation)
                .font(.body)
                .foregroundColor(.secondary)
        }
        .padding()
        .frame(maxWidth: .infinity, alignment: .leading)
        .background(Color.gray.opacity(0.1))
        .cornerRadius(10)
        .padding(.top)
    }
}

// View hiển thị kết quả cuối cùng
struct ResultView: View {
    let score: Int
    let total: Int
    let action: () -> Void
    
    var body: some View {
        VStack(spacing: 20) {
            Image(systemName: "trophy.fill")
                .font(.system(size: 80))
                .foregroundColor(.yellow)
            
            Text("Hoàn thành!")
                .font(.largeTitle)
                .fontWeight(.bold)
            
            Text("Bạn trả lời đúng \(score) / \(total) câu hỏi.")
                .font(.title3)
            
            Button(action: action) {
                Text("Làm lại")
                    .padding()
                    .frame(maxWidth: 200)
                    .background(Color.blue)
                    .foregroundColor(.white)
                    .cornerRadius(10)
            }
        }
    }
}
