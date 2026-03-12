import Foundation

struct Question: Identifiable, Codable {
    let id: Int
    let topic: String
    let question: String
    let options: [String: String]
    let answer: String
    let explanation: String
    
    // Helper để lấy danh sách các lựa chọn được sắp xếp
    var sortedOptions: [(key: String, value: String)] {
        options.sorted { $0.key < $1.key }
    }
}

enum Topic: String, CaseIterable {
    case to_tung_hinh_su = "to_tung_hinh_su"
    case dao_duc_nghe_nghiep = "dao_duc_nghe_nghiep"
    case to_tung_dan_su = "to_tung_dan_su"
    case hanh_chinh = "hanh_chinh"
    
    var displayName: String {
        switch self {
        case .to_tung_hinh_su: return "Tố tụng hình sự"
        case .dao_duc_nghe_nghiep: return "Đạo đức nghề nghiệp"
        case .to_tung_dan_su: return "Tố tụng dân sự"
        case .hanh_chinh: return "Hành chính"
        }
    }
}
