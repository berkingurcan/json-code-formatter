'use client'

import Formatter from '@/components/formatter'
import { Button } from '@mui/material'
import Head from 'next/head'
import Link from 'next/link'
import { useState } from 'react'

export default function Home() {

  const [editorValue, setEditorValue] = useState('');
  const [formattedValue, setFormattedValue] = useState('');
  
    // use @app.route("/api/python") with input editorValue in this function

  function format(): void {
    console.log('formatting')
    console.log(editorValue)

    fetch('/api/python', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({ editorValue: editorValue }),
    })
      .then(response => response.json())
      .then(data => {
        console.log('Formatted value:', data);
        setFormattedValue(data.formattedValue);
      })
      .catch(error => {
        console.error('Error:', error);
      });
  }

  function handleEditorChange(value: any) {
    setEditorValue(value);
  }

  return (
    <main style={{ display: 'grid'}}>
        <div style={{ display: 'grid', gridTemplateColumns: '1fr 1fr', gridGap: '20px' }}>
            <Formatter onEditorChange={handleEditorChange} />
            <div>
              <h1>{formattedValue}</h1>
            </div>
        </div>
        <div style={{ display: 'flex', justifyContent: 'center' }}>
          <Button variant="outlined" onClick={format}>Format :D</Button>
        </div>
    </main>
  )
}
