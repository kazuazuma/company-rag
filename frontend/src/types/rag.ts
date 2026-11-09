export interface RAGRequest {
    question: string;
}

export interface SourceDocument {
    id: number;
    title: string;
    content: string;
    score: number;
}

export interface RAGResponse {
    answer: string;
    sources: SourceDocument[];
}
