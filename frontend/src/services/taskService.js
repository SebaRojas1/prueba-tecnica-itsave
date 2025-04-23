import axiosClient from "@/utils/axiosClient";

export const getTasks = () => axiosClient.get("/tasks");

export const addTask = (task) => axiosClient.post("/tasks/add/", task);

export const deleteTask = (id) => axiosClient.delete(`/tasks/${id}/delete/`);

export const markTask = (id) => axiosClient.patch(`/tasks/${id}/complete/`);
