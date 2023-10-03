import './App.css'
import { useState } from 'react'
import Axios from 'axios'


function App() {
  const [message, setMessage] = useState('')
  const messageClass = message === 'Valid credit card' ? 'Valid' : 'Invalid'


  const handleSubmit = (e) => {
    e.preventDefault()

    const cardNumber = document.getElementById('cardNumber').value
    const expirationDate = document.getElementById('expirationDate').value
    const cvv = document.getElementById('cvv').value

    Axios.post('http://localhost:8000/credit-card', {
      number: cardNumber,
      expiration_date: expirationDate,
      cvv: cvv,
    }).then((response) => {
      console.log(response.data)
      setMessage('Valid credit card')
    }).catch((error) => {
      console.log(error.response.data.detail)
      setMessage(error.response.data.detail)
    })


  }

  return (
    <div className="App">
        <form className='Form' onSubmit={handleSubmit}>
          <h1>Credit Card Validation</h1>
          <label for="username">Card Number:</label>
          <input className='Input' type="text" id="cardNumber" required/> 
          <label for="username">Expiration Date (YYYY-MM):</label>
          <input className='Input' type="text" id="expirationDate" required/> 
          <label for="username">CVV:</label>
          <input className='Input' type="text" id="cvv" required/> 
          <button className='Button' type="submit">Submit</button>
          <p className={messageClass}>{message}</p>
          
        </form>
    </div>
  )
}

export default App
