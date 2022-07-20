import React, { useContext, useEffect, useState } from 'react'
import '../pagesCSS/Home.css'
import Button from '@mui/material/Button';
import TextField from '@mui/material/TextField';
import axios from 'axios';
import Content from './Content'


function Home() {
  const [search , setSearch] = useState()
  const [mangas , setMangas] = useState([])
  
  const handleSubmit = () => {
    if(mangas.length === 0){
      axios.post('http://127.0.0.1:5000/request_manga' , {
        search: search
      }).then((res) => {
        setMangas(res.data)
      })
    }else{
      mangas.length = 0
      handleSubmit()
    }
  
  }

  return(
    <>

      <div className='container'>
        <div className='inputArea'>
          <TextField
            label='Pesquisar'
            variant="standard"
            className="search"
            onChange={(e) => {
            e.preventDefault()
              setSearch(e.target.value)
            }}
          />

          <Button className="botao" onClick={handleSubmit}> ENVIAR </Button>
        </div>

        <Content content={mangas} />
      </div>

  </>
  )
}

export default Home;
