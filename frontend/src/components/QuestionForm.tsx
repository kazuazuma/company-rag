import { useState } from "react";
import type { SyntheticEvent } from "react";

interface Props {
    onSubmit: (question: string) => Promise<void>;
    loading: boolean;
}

export function QuestionForm({
    onSubmit,
    loading,
}: Props) {
    const[question, setQuestion] = useState("");

    async function handleSubmit(
        event: SyntheticEvent<HTMLFormElement, SubmitEvent>
    ){
        event.preventDefault();

        const trimmed = question.trim();

        if (!trimmed || loading) return;

        await onSubmit(trimmed);
    }

    return (
        <form onSubmit={handleSubmit}>
            <label htmlFor="question">
                社内ルールについて質問する
            </label>

            <textarea
                id="question"
                value={question}
                onChange={(event) =>
                    setQuestion(event.target.value)
                }
                placeholder="有給休暇は何日前までに申請しますか？"
                maxLength={2000}
                rows={4}
                required
            />

            <button
                type="submit"
                disabled={loading || !question.trim()}
            >
                {loading ? "回答を生成中..." : "質問をする"}
            </button>
        </form>
    );
}