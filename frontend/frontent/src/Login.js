import './App.css';
import React, { useContext, useState } from 'react'
import Button from '@mui/material/Button';
import TextField from '@mui/material/TextField';
import Grid from '@mui/material/Grid';

import AuthContext from './context/auth'
import Typography from '@mui/material/Typography';


function Login() {
  const loginData = useContext(AuthContext)
  const [email, setEmail] = useState('')
  const [senha, setSenha] = useState('')
  const [erroStatus, setErroStatus] = useState(false)

  let status = true

  const emailEsenhaExiste = () => {
    if (email && senha) {
      status = true
      setErroStatus(false)
    } else {
      status = false
      setErroStatus(true)
    }
  }

  const verifica = () => {
    emailEsenhaExiste()
    if (status === true) {
      if (email.match(/@/) && email.match(/.com/)) {
        status = true
        setErroStatus(false)
      } else {
        status = false
        setErroStatus(true)
      }
    } else {
      status = false
      setErroStatus(true)
    }
  }

  const handleSubmit = async () => {
    verifica()
    if (status === true) {
      try {
        await loginData.logIn(email, senha) 
        //console.log(loginData.user.nome)
        alert(`Logado ${loginData.user.nome}`)
      } catch (error) {
       alert(error)
        
      }

    } else {
      alert('Dados inválidos, tente novamente')
    }
  }
  return (
    <>

      <Grid container className='containerC'>
        <Grid
          container
          justifyContent='center'
          alignItems='center'
          direction='column'
          className='titleContainer'
        >

          <Typography variant='h4'> Login </Typography>
          <><h4>   </h4></>
          <TextField
            label='Email'
            error={erroStatus}
            className='emailText'
            variant="standard"
            onChange={(e) => {
              e.preventDefault()
              setEmail(e.target.value)
            }}
          />
          <><h1>    </h1></>
          <TextField
            label='Senha'
            error={erroStatus}
            type='password'
            className='senhaText'
            variant="standard"
            onChange={(e) => {
              e.preventDefault()
              setSenha(e.target.value)
            }}
          />
          <><h1>    </h1></>
          <Button className="botao" onClick={handleSubmit}> ENTRAR </Button>

        </Grid>
      </Grid>
    </>
  );
}

export default Login;
