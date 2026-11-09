import type { RAGResponse } from "../types/rag";

interface Props {
    result: RAGResponse;
}

export function AnswerCard({ result }: Props) {
    return (
        <section>
            <h2>AIの回答</h2>

            <p>{result.answer}</p>

            <h3>参照資料</h3>

            {result.sources.length === 0 ? (
                <p>参照資料はありません</p>
            ) : (
                <ul>
                    {result.sources.map((source) => (
                        <li key={source.id}>
                            <strong>{source.title}</strong>

                            <p>{source.content}</p>

                            <small>
                                類似度: {source.score.toFixed(3)}
                            </small>
                        </li>
                    ))}
                </ul>
            )}
        </section>
    );
}