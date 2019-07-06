config:{
  "name": "CPFLMudanca",
  "intents": [
    {
      "intent": "informacao_alterar_titularidade",
      "examples": [
        {
          "text": "Gostaria de mais informações sobre alterar a titularidade"
        },
        {
          "text": "Tenho duvidas sobre alteração de titularidade"
        },
        {
          "text": "Como faço para alterar a titularidade ?"
        },
        {
          "text": "Gostaria de saber mais sobre como mudar a titularidade"
        },
        {
          "text": "Como altero a titularidade ?"
        },
        {
          "text": "Como faço isso ?"
        }
      ],
      "description": "Intenção de buscar informação sobre alterar a titularidade"
    },
    {
      "intent": "alterar_titularidade",
      "examples": [
        {
          "text": "Vou trocar a titularidade"
        },
        {
          "text": "Mudança de titularidade"
        },
        {
          "text": "Gostaria de mudar a titularidade"
        },
        {
          "text": "Vou me mudar e preciso trocar a titularidade"
        },
        {
          "text": "Trocar titularidade"
        },
        {
          "text": "Mudar titularidade"
        },
        {
          "text": "Alterar titularidade"
        }
      ],
      "description": "Capturar interesse em mudar a titularidade"
    },
    {
      "intent": "informacao_nova_instalacao",
      "examples": [
        {
          "text": "Como faço para pedir uma nova instalação"
        },
        {
          "text": "O que eu faço pra ter uma nova instalação"
        },
        {
          "text": "Tenho duvidas de como pedir uma nova instalação"
        },
        {
          "text": "Como peço uma nova instalação ?"
        },
        {
          "text": "Como faço uma nova instalação"
        },
        {
          "text": "Como é esse role de nova instalação ?"
        },
        {
          "text": "Tenho duvidas de como pedir uma nova instalção"
        }
      ],
      "description": "Intenção de coletar informação para nova instalação"
    },
    {
      "intent": "boas_vindas",
      "examples": [
        {
          "text": "Opa"
        },
        {
          "text": "Olá"
        },
        {
          "text": "Oi"
        }
      ],
      "description": "Boas vindas"
    },
    {
      "intent": "fazer_mudanca",
      "examples": [
        {
          "text": "Trocar minha conta"
        },
        {
          "text": "Vou me mudar"
        },
        {
          "text": "Estou me mudando"
        },
        {
          "text": "Preciso me mudar"
        },
        {
          "text": "Preciso trocar meu endereço"
        },
        {
          "text": "Estou de mudança"
        },
        {
          "text": "Mudar minha conta"
        },
        {
          "text": "Mudar meu endereço"
        }
      ],
      "description": "Inteção de estar de mudança"
    },
    {
      "intent": "despedida",
      "examples": [
        {
          "text": "Muito obrigado, tchau"
        },
        {
          "text": "Isso é tudo, obrigado"
        },
        {
          "text": "Não preciso fazer mais nada, obrigado"
        },
        {
          "text": "Já resolvi meu problema"
        },
        {
          "text": "Tchau"
        },
        {
          "text": "Adeus"
        },
        {
          "text": "Finalizar"
        },
        {
          "text": "Fim"
        },
        {
          "text": "Acabar"
        }
      ],
      "description": "Finalização da iteração"
    },
    {
      "intent": "nova_instalacao",
      "examples": [
        {
          "text": "Preciso de uma nova instalação"
        },
        {
          "text": "Vou fazer uma nova instalação"
        },
        {
          "text": "Vou me mudar para uma casa nova e preciso fazer uma nova instalação"
        },
        {
          "text": "Gostaria de requisitar uma nova instalação"
        }
      ],
      "description": "Intenção de nova instalação"
    }
  ],
  "entities": [],
  "language": "pt-br",
  "metadata": {
    "api_version": {
      "major_version": "v1",
      "minor_version": "2018-09-20"
    }
  },
  "description": "",
  "dialog_nodes": [
    {
      "type": "standard",
      "title": "Bem-vindo padrão",
      "output": {
        "generic": [
          {
            "values": [
              {
                "text": "Olá. Como posso ajudar ?"
              }
            ],
            "response_type": "text",
            "selection_policy": "sequential"
          }
        ]
      },
      "metadata": {},
      "conditions": "#boas_vindas",
      "dialog_node": "node_1_1562424491311",
      "previous_sibling": "Bem-vindo"
    },
    {
      "type": "standard",
      "title": "Em outros casos",
      "output": {
        "generic": [
          {
            "values": [
              {
                "text": "Eu não entendi. Você pode tentar reformular a frase."
              },
              {
                "text": "Você pode reformular sua afirmação? Eu não estou entendendo."
              },
              {
                "text": "Eu não entendi o sentido."
              }
            ],
            "response_type": "text",
            "selection_policy": "sequential"
          }
        ]
      },
      "metadata": {},
      "conditions": "anything_else",
      "dialog_node": "Em outros casos",
      "previous_sibling": "node_1_1562424491311"
    },
    {
      "type": "standard",
      "title": "Bem-vindo",
      "output": {
        "generic": [
          {
            "values": [
              {
                "text": "Opa, beleza ? Como posso te ajudar?"
              },
              {
                "text": "Oie, como posso te ajudar ?"
              }
            ],
            "response_type": "text",
            "selection_policy": "sequential"
          }
        ]
      },
      "metadata": {},
      "conditions": "#boas_vindas && $noob",
      "dialog_node": "Bem-vindo"
    }
  ],
  "workspace_id": "0f156808-de0f-4c7c-a97f-408808cabe79",
  "counterexamples": [],
  "system_settings": {
    "tooling": {
      "store_generic_responses": true
    }
  },
  "learning_opt_out": false,
  "status": "Available"
}