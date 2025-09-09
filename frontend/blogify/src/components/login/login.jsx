import React from 'react';
import { Button, Checkbox, Form, Input, message } from 'antd';
import axios from 'axios';

const Login = () => {
  const onFinish = async (values) => {
    try {
      const response = await axios.post('http://127.0.0.1:8000/api/accounts/login/', {
        username: values.username,
        password: values.password,
      });

      console.log('Login success:', response.data);

      // Store tokens in localStorage
      localStorage.setItem('access_token', response.data.access);
      localStorage.setItem('refresh_token', response.data.refresh);

      message.success('Login successful!');

      // Optional: Redirect to dashboard or home
      // window.location.href = '/dashboard';

    } catch (error) {
      console.error('Login failed:', error.response?.data);
      message.error(error.response?.data.error || 'Login failed');
    }
  };

  const onFinishFailed = (errorInfo) => {
    console.log('Failed:', errorInfo);
  };

  return (
    <Form
      name="loginForm"
      labelCol={{ span: 8 }}
      wrapperCol={{ span: 16 }}
      style={{ maxWidth: 600 }}
      initialValues={{ remember: true }}
      onFinish={onFinish}
      onFinishFailed={onFinishFailed}
      autoComplete="off"
    >
      <Form.Item
        label="Username"
        name="username"
        rules={[{ required: true, message: 'Please input your username!' }]}
      >
        <Input />
      </Form.Item>

      <Form.Item
        label="Password"
        name="password"
        rules={[{ required: true, message: 'Please input your password!' }]}
      >
        <Input.Password />
      </Form.Item>

      <Form.Item name="remember" valuePropName="checked" label={null}>
        <Checkbox>Remember me</Checkbox>
      </Form.Item>

      <Form.Item label={null}>
        <Button type="primary" htmlType="submit">
          Login
        </Button>
      </Form.Item>
    </Form>
  );
};

export default Login;
