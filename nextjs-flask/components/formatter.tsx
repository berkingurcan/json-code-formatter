import React from 'react';
import Link from 'next/link'
import Editor from '@monaco-editor/react';

export default function Formatter({onEditorChange}: any) {
    function handleEditorChange(value: any, _event: any) {
        onEditorChange(value);
    }

    return (
        <Editor 
            height="90vh" 
            width="80%"
            defaultLanguage="rust" 
            defaultValue="// some comment" 
            onChange={handleEditorChange}
        />
    )
}
