Rails.application.routes.draw do
  root to: 'pages#home'
  namespace :api, defaults: { format: :json } do
    namespace :v1 do
      # resources :chatbot, only: [:create]
      post '/parse', to: 'responses#parse'
      get '/answer', to: 'responses#answer'
    end
  end
end
