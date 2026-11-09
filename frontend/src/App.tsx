import { useState } from "react";

import { askRAG } from "./api/rag";
import { QuestionForm } from "./components/QuestionForm";
import { AnswerCard } from "./components/AnswerCard";

import type { RAGResponse } from "./types/rag";

import "./index.css";

export default function App() {
  const [result, setResult] =
    useState<RAGResponse | null>(null);

  const [loading, setLoading] = useState(false);

  const [error, setError] = useState<string | null>(null);
  
  async function handleAsk(question: string) {
    setLoading(true);
    setError(null);
    setResult(null);

    try {
      const data = await askRAG(question);

      setResult(data);
    } catch (err) {
      console.error(err);

      setError(
        "回答の取得に失敗しました。時間を置いて再試行して下さい。"
      );
    } finally {
      setLoading(false);
    }
  }

  return (
    <main className="container">
      <h1>Company Knowledge AI</h1>

      <p>社内ナレッジ検索アシスタント</p>

      <QuestionForm
        onSubmit={handleAsk}
        loading={loading}
      />

      {error && (
        <p role="alert" className="error">
          {error}
        </p>
      )}

      {result && <AnswerCard result={result} />}
    </main>
  );
}