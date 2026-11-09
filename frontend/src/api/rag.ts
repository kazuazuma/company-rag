import type {
    RAGRequest,
    RAGResponse,
} from "../types/rag";

const API_BASE_URL =
    import.meta.env.VITE_API_BASE_URL ??
    "http://localhost:8000";

export async function askRAG(
    question: string
): Promise<RAGResponse> {
    const request: RAGRequest = {
        question,
    };

    const response = await fetch(
        `${API_BASE_URL}/rag/ask`,
        {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify(request),
        }
    );

    if (!response.ok) {
        throw new Error(
            `API error: ${response.status}`
        );
    }

    return (await response.json()) as RAGResponse;
}