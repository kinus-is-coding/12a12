import Form from "../components/Form"

function Login() {
    console.log("cloz mas")
    return <Form route="/api/token/" method="login" />
}

export default Login