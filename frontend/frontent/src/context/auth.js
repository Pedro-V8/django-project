import React, { createContext, useState } from 'react'
import axios from 'axios';


const AuthContext = createContext({})

export function AuthProvider({ children }) {
    const [user, setUser] = useState(() => {
        const userString = localStorage.getItem('user')

        if (userString) {
            return JSON.parse(userString)
        }

        return null
    })

    const [token, setToken] = useState(localStorage.getItem('token'))

    const logIn = async (email, senha) => {
        let response

        try {
            response = await axios.post('http://localhost:8000/users/login/', {
                email: email,
                password: senha,
            })
                .then(({ data, status }) => {
                    console.log(data)
                    const obj = { data, status }
                    return obj
                })
        } catch (error) {
            throw new Error(`Erro ao fazer login, email ou senha incorretos... \nLog: ${error}`)
        }

        if (response && response.status === 200) {
            localStorage.setItem('user', JSON.stringify(response.data.user))
            localStorage.setItem('token', response.data.token)

            setUser(() => {
                const userString = localStorage.getItem('user')

                if (userString) {
                    return JSON.parse(userString)
                }

                return null
            })

            setToken(localStorage.getItem('token'))
        }
    }


    return (
        <AuthContext.Provider value={{ signed: !!user, user, token, logIn }}>
            {children}
        </AuthContext.Provider>
    )
}

export default AuthContext