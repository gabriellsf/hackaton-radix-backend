data = {
  "name": "CPFLMudanca",
  "intents": [
    {
      "intent": "discordancia",
      "examples": [
        {
          "text": "Nah"
        },
        {
          "text": "No"
        },
        {
          "text": "Nunca"
        },
        {
          "text": "Não preciso"
        },
        {
          "text": "Não"
        }
      ],
      "description": ""
    },
    {
      "intent": "concordar",
      "examples": [
        {
          "text": "Vamos"
        },
        {
          "text": "Com certeza"
        },
        {
          "text": "si"
        },
        {
          "text": "Uhum"
        },
        {
          "text": "Sim"
        },
        {
          "text": "Claro"
        }
      ],
      "description": ""
    },
    {
      "intent": "informacao_alterar_titularidade",
      "examples": [
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
        },
        {
          "text": "Gostaria de mais informações sobre alterar a titularidade"
        }
      ],
      "description": "Intenção de buscar informação sobre alterar a titularidade"
    },
    {
      "intent": "alterar_titularidade",
      "examples": [
        {
          "text": "Vou me mudar e preciso trocar a titularidade"
        },
        {
          "text": "Gostaria de mudar a titularidade"
        },
        {
          "text": "Alterar titularidade"
        },
        {
          "text": "Vou trocar a titularidade"
        },
        {
          "text": "Mudança de titularidade"
        },
        {
          "text": "Mudar titularidade"
        },
        {
          "text": "Trocar titularidade"
        }
      ],
      "description": "Capturar interesse em mudar a titularidade"
    },
    {
      "intent": "informacao_nova_instalacao",
      "examples": [
        {
          "text": "Como peço uma nova instalação ?"
        },
        {
          "text": "Tenho duvidas de como pedir uma nova instalção"
        },
        {
          "text": "Tenho duvidas de como pedir uma nova instalação"
        },
        {
          "text": "Como faço para pedir uma nova instalação"
        },
        {
          "text": "Como faço uma nova instalação"
        },
        {
          "text": "O que eu faço pra ter uma nova instalação"
        },
        {
          "text": "Como é esse role de nova instalação ?"
        }
      ],
      "description": "Intenção de coletar informação para nova instalação"
    },
    {
      "intent": "boas_vindas",
      "examples": [
        {
          "text": "Oi"
        },
        {
          "text": "Opa"
        },
        {
          "text": "Olá"
        }
      ],
      "description": "Boas vindas"
    },
    {
      "intent": "fazer_mudanca",
      "examples": [
        {
          "text": "Estou me mudando"
        },
        {
          "text": "Mudar meu endereço"
        },
        {
          "text": "Mudar minha conta"
        },
        {
          "text": "Trocar minha conta"
        },
        {
          "text": "Estou de mudança"
        },
        {
          "text": "Preciso trocar meu endereço"
        },
        {
          "text": "Preciso me mudar"
        },
        {
          "text": "Vou me mudar"
        }
      ],
      "description": "Inteção de estar de mudança"
    },
    {
      "intent": "despedida",
      "examples": [
        {
          "text": "Já resolvi meu problema"
        },
        {
          "text": "Isso é tudo, obrigado"
        },
        {
          "text": "Fim"
        },
        {
          "text": "Acabar"
        },
        {
          "text": "Muito obrigado, tchau"
        },
        {
          "text": "Não preciso fazer mais nada, obrigado"
        },
        {
          "text": "Tchau"
        },
        {
          "text": "Adeus"
        },
        {
          "text": "Finalizar"
        }
      ],
      "description": "Finalização da iteração"
    },
    {
      "intent": "nova_instalacao",
      "examples": [
        {
          "text": "Gostaria de requisitar uma nova instalação"
        },
        {
          "text": "Vou fazer uma nova instalação"
        },
        {
          "text": "Vou me mudar para uma casa nova e preciso fazer uma nova instalação"
        },
        {
          "text": "Preciso de uma nova instalação"
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
      "title": "Sucesso",
      "output": {
        "generic": [
          {
            "values": [
              {
                "text": "Já tenho todas as informações que preciso! Em breve ligaremos confirmando a sua instalação.\n"
              }
            ],
            "response_type": "text",
            "selection_policy": "sequential"
          }
        ]
      },
      "parent": "node_44_1562450814267",
      "metadata": {},
      "conditions": "#concordar",
      "dialog_node": "node_45_1562450814267"
    },
    {
      "type": "standard",
      "title": "Falha",
      "output": {
        "generic": [
          {
            "values": [
              {
                "text": "Poxa a essa foto não ficou muito boa, poderia tentar tirar outra com mais luz sobre o contrato."
              }
            ],
            "response_type": "text",
            "selection_policy": "sequential"
          }
        ]
      },
      "parent": "node_42_1562450814267",
      "metadata": {},
      "conditions": "#discordancia",
      "dialog_node": "node_47_1562450814267",
      "previous_sibling": "node_43_1562450814267"
    },
    {
      "type": "standard",
      "title": "Sucesso",
      "output": {
        "generic": [
          {
            "values": [
              {
                "text": "Já tenho todas as informações que preciso! Em breve ligaremos confirmando a alteração da titularidade."
              }
            ],
            "response_type": "text",
            "selection_policy": "sequential"
          }
        ]
      },
      "parent": "node_42_1562450814267",
      "metadata": {},
      "conditions": "#concordar",
      "dialog_node": "node_43_1562450814267"
    },
    {
      "type": "standard",
      "title": "Informa foto Poste",
      "output": {
        "generic": [
          {
            "values": [
              {
                "text": "$foto_poste\n"
              }
            ],
            "response_type": "text",
            "selection_policy": "sequential"
          }
        ]
      },
      "parent": "node_16_1562448280556",
      "metadata": {},
      "dialog_node": "node_19_1562450010961"
    },
    {
      "type": "standard",
      "title": "Nova tentativa foto",
      "output": {
        "generic": []
      },
      "parent": "node_47_1562450814267",
      "metadata": {},
      "next_step": {
        "behavior": "jump_to",
        "selector": "condition",
        "dialog_node": "node_42_1562450814267"
      },
      "dialog_node": "node_48_1562450814267"
    },
    {
      "type": "standard",
      "title": "Informa Endereço",
      "output": {
        "generic": [
          {
            "values": [
              {
                "text": "Ótimo, agora preciso só que me confirme sua identidade. Pode me mandar uma foto sua segurando seu RG (com a foto pra camera) ?\n"
              }
            ],
            "response_type": "text",
            "selection_policy": "sequential"
          }
        ]
      },
      "parent": "node_8_1562444129830",
      "metadata": {},
      "dialog_node": "node_10_1562444690765"
    },
    {
      "type": "standard",
      "title": "Informa Endereço",
      "output": {
        "generic": [
          {
            "values": [
              {
                "text": "Ótimo, agora preciso só que me confirme sua identidade. Pode me mandar uma foto sua segurando seu RG (com a foto pra camera) ?\n"
              }
            ],
            "response_type": "text",
            "selection_policy": "sequential"
          }
        ]
      },
      "parent": "node_38_1562450814267",
      "metadata": {},
      "dialog_node": "node_39_1562450814267"
    },
    {
      "type": "standard",
      "title": "Nova tentativa foto",
      "output": {
        "generic": []
      },
      "parent": "node_17_1562448380109",
      "metadata": {},
      "next_step": {
        "behavior": "jump_to",
        "selector": "condition",
        "dialog_node": "node_15_1562448230932"
      },
      "dialog_node": "node_18_1562449817771"
    },
    {
      "type": "standard",
      "title": "Discordar da ajuda",
      "output": {
        "generic": [
          {
            "values": [
              {
                "text": "Beleza! Para qual endereço você vai se mudar ?"
              },
              {
                "text": "Para onde você vai se mudar ?"
              }
            ],
            "response_type": "text",
            "selection_policy": "sequential"
          }
        ]
      },
      "parent": "node_5_1562443608008",
      "metadata": {},
      "conditions": "#discordancia",
      "dialog_node": "node_8_1562444129830",
      "previous_sibling": "node_6_1562443920290"
    },
    {
      "type": "standard",
      "title": "Concordar com ajuda",
      "output": {
        "generic": []
      },
      "parent": "node_5_1562443608008",
      "metadata": {},
      "next_step": {
        "behavior": "jump_to",
        "selector": "body",
        "dialog_node": "node_5_1562440537446"
      },
      "conditions": "#concordar",
      "dialog_node": "node_6_1562443920290"
    },
    {
      "type": "standard",
      "title": "Não",
      "output": {
        "generic": [
          {
            "values": [
              {
                "text": "Então você quer criar uma nova instalação!"
              },
              {
                "text": "Então você quer abrir uma nova instalação. Beleza, vamos lá"
              }
            ],
            "response_type": "text",
            "selection_policy": "sequential"
          }
        ]
      },
      "parent": "node_51_1562451061284",
      "metadata": {},
      "next_step": {
        "behavior": "jump_to",
        "selector": "body",
        "dialog_node": "node_5_1562443608008"
      },
      "conditions": "#discordancia",
      "dialog_node": "node_53_1562451235104",
      "previous_sibling": "node_52_1562451160870"
    },
    {
      "type": "standard",
      "title": "Sim",
      "output": {
        "generic": [
          {
            "values": [
              {
                "text": "Então você quer trocar sua titularidade! Vamos lá"
              }
            ],
            "response_type": "text",
            "selection_policy": "sequential"
          }
        ]
      },
      "parent": "node_51_1562451061284",
      "metadata": {},
      "next_step": {
        "behavior": "jump_to",
        "selector": "body",
        "dialog_node": "node_36_1562450814265"
      },
      "conditions": "#concordar",
      "dialog_node": "node_52_1562451160870"
    },
    {
      "type": "standard",
      "title": "Discordar da ajuda",
      "output": {
        "generic": [
          {
            "values": [
              {
                "text": "Beleza! Para qual endereço você vai se mudar ?"
              },
              {
                "text": "Para onde você vai se mudar ?"
              }
            ],
            "response_type": "text",
            "selection_policy": "sequential"
          }
        ]
      },
      "parent": "node_36_1562450814265",
      "metadata": {},
      "conditions": "#discordancia",
      "dialog_node": "node_38_1562450814267",
      "previous_sibling": "node_37_1562450814267"
    },
    {
      "type": "standard",
      "title": "Concordar da ajuda",
      "output": {
        "generic": []
      },
      "parent": "node_36_1562450814265",
      "metadata": {},
      "next_step": {
        "behavior": "jump_to",
        "selector": "body",
        "dialog_node": "node_22_1562450487430"
      },
      "conditions": "#concordar",
      "dialog_node": "node_37_1562450814267"
    },
    {
      "type": "standard",
      "title": "Concordar",
      "output": {
        "generic": [
          {
            "values": [],
            "response_type": "text",
            "selection_policy": "sequential"
          }
        ]
      },
      "parent": "node_5_1562440537446",
      "metadata": {},
      "next_step": {
        "behavior": "jump_to",
        "selector": "body",
        "dialog_node": "node_8_1562444129830"
      },
      "conditions": "#concordar",
      "dialog_node": "node_9_1562444357961"
    },
    {
      "type": "standard",
      "title": "Informa Foto Contrato",
      "output": {
        "generic": [
          {
            "values": [
              {
                "text": "$foto_contrato"
              }
            ],
            "response_type": "text",
            "selection_policy": "sequential"
          }
        ]
      },
      "parent": "node_41_1562450814267",
      "metadata": {},
      "dialog_node": "node_42_1562450814267"
    },
    {
      "type": "standard",
      "title": "Informa foto Poste",
      "output": {
        "generic": [
          {
            "values": [
              {
                "text": "$foto_poste\n"
              }
            ],
            "response_type": "text",
            "selection_policy": "sequential"
          }
        ]
      },
      "parent": "node_43_1562450814267",
      "metadata": {},
      "dialog_node": "node_44_1562450814267"
    },
    {
      "type": "standard",
      "title": "Falha",
      "output": {
        "generic": [
          {
            "values": [
              {
                "text": "Poxa a foto não ficou muito boa, poderia tentar tirar outra em um local mais claro ?"
              }
            ],
            "response_type": "text",
            "selection_policy": "sequential"
          }
        ]
      },
      "parent": "node_40_1562450814267",
      "metadata": {},
      "conditions": "#discordancia",
      "dialog_node": "node_49_1562450814267",
      "previous_sibling": "node_41_1562450814267"
    },
    {
      "type": "standard",
      "title": "Sucesso",
      "output": {
        "generic": [
          {
            "values": [
              {
                "text": "Ficou ótimo, conseguimos te ver bem. Você poderia mandar uma foto do contrato da casa, contrato de aluguel ou algo do tipo ?\n"
              }
            ],
            "response_type": "text",
            "selection_policy": "sequential"
          }
        ]
      },
      "parent": "node_40_1562450814267",
      "metadata": {},
      "conditions": "#concordar",
      "dialog_node": "node_41_1562450814267"
    },
    {
      "type": "standard",
      "title": "Requisitar nova titularidade",
      "output": {
        "generic": [
          {
            "values": [
              {
                "text": "Claro.  você precisa de ajuda para fazer isso ?"
              },
              {
                "text": "Claro, você quer detalhes do que precisa ?"
              }
            ],
            "response_type": "text",
            "selection_policy": "sequential"
          }
        ]
      },
      "parent": "node_1_1562441885816",
      "metadata": {},
      "conditions": "#alterar_titularidade",
      "dialog_node": "node_36_1562450814265",
      "previous_sibling": "node_5_1562443608008"
    },
    {
      "type": "standard",
      "title": "Informação nova titularidade",
      "output": {
        "generic": [
          {
            "values": [
              {
                "text": "Vamos lá, para fazer a nova titularidade é um processo bem simples, precisamos da sua identidade, o endereço e algum comprovante da sua casa nova, só isso. Quer fazer isso agora ?"
              },
              {
                "text": ""
              }
            ],
            "response_type": "text",
            "selection_policy": "sequential"
          }
        ]
      },
      "parent": "node_1_1562441885816",
      "metadata": {},
      "conditions": "#informacao_alterar_titularidade",
      "dialog_node": "node_22_1562450487430",
      "previous_sibling": "node_36_1562450814265"
    },
    {
      "type": "standard",
      "title": "Requisitar nova instalação",
      "output": {
        "generic": [
          {
            "values": [
              {
                "text": "Claro. Você sabe como fazer isso ?"
              },
              {
                "text": "Claro, você quer detalhes do que precisa ?"
              }
            ],
            "response_type": "text",
            "selection_policy": "sequential"
          }
        ]
      },
      "parent": "node_1_1562441885816",
      "metadata": {},
      "conditions": "#nova_instalacao",
      "dialog_node": "node_5_1562443608008",
      "previous_sibling": "node_5_1562440537446"
    },
    {
      "type": "standard",
      "title": "Informação nova instalação",
      "output": {
        "generic": [
          {
            "values": [
              {
                "text": "Vou te explicar como funciona. Primeiro você precisa confirmar que realmente não há energia no local.  Se realmente não houver, por favor certifique-se se há um posto aderente a regulamentação na proximidade.  Pronto para começar o processo ?"
              }
            ],
            "response_type": "text",
            "selection_policy": "sequential"
          }
        ]
      },
      "parent": "node_1_1562441885816",
      "metadata": {},
      "conditions": "#informacao_nova_instalacao",
      "dialog_node": "node_5_1562440537446",
      "previous_sibling": "Bem-vindo"
    },
    {
      "type": "standard",
      "title": "Mudança Duvida",
      "output": {
        "generic": [
          {
            "values": [
              {
                "text": "Alguem mora no endereço atualmente ? Preciso saber se lá já possui uma instalação elétrica atualmente."
              }
            ],
            "response_type": "text",
            "selection_policy": "sequential"
          }
        ]
      },
      "parent": "node_1_1562441885816",
      "metadata": {},
      "conditions": "#fazer_mudanca",
      "dialog_node": "node_51_1562451061284",
      "previous_sibling": "node_22_1562450487430"
    },
    {
      "type": "standard",
      "title": "Bem-vindo Noob",
      "output": {
        "generic": [
          {
            "values": [
              {
                "text": "Tudo certo ? Como posso te ajudar?"
              },
              {
                "text": "Tudo tranquilo ? Como posso te ajudar ?"
              }
            ],
            "response_type": "text",
            "selection_policy": "random"
          }
        ]
      },
      "parent": "node_1_1562441885816",
      "metadata": {},
      "conditions": "#boas_vindas",
      "dialog_node": "Bem-vindo"
    },
    {
      "type": "standard",
      "title": "Sucesso",
      "output": {
        "generic": [
          {
            "values": [
              {
                "text": "Já tenho todas as informações que preciso! Em breve ligaremos confirmando a sua instalação.\n"
              }
            ],
            "response_type": "text",
            "selection_policy": "sequential"
          }
        ]
      },
      "parent": "node_19_1562450010961",
      "metadata": {},
      "conditions": "#concordar",
      "dialog_node": "node_20_1562450179763"
    },
    {
      "type": "standard",
      "title": "Falha",
      "output": {
        "generic": [
          {
            "values": [
              {
                "text": "Poxa a essa foto não ficou muito boa, poderia tentar tirar outra com mais luz sobre o contrato."
              }
            ],
            "response_type": "text",
            "selection_policy": "sequential"
          }
        ]
      },
      "parent": "node_15_1562448230932",
      "metadata": {},
      "conditions": "#discordancia",
      "dialog_node": "node_17_1562448380109",
      "previous_sibling": "node_16_1562448280556"
    },
    {
      "type": "standard",
      "title": "Sucesso",
      "output": {
        "generic": [
          {
            "values": [
              {
                "text": "Perfeito, só precisamos de mais uma informação. O poste próximo precisa estar de acordo com nosso regulamento. Poderia tirar uma foto para verificarmos se ele está de acordo."
              }
            ],
            "response_type": "text",
            "selection_policy": "sequential"
          }
        ]
      },
      "parent": "node_15_1562448230932",
      "metadata": {},
      "conditions": "#concordar",
      "dialog_node": "node_16_1562448280556"
    },
    {
      "type": "standard",
      "title": "Informa foto Identidade",
      "output": {
        "generic": [
          {
            "values": [
              {
                "text": "$foto_identidade"
              }
            ],
            "response_type": "text",
            "selection_policy": "sequential"
          }
        ]
      },
      "parent": "node_39_1562450814267",
      "metadata": {},
      "dialog_node": "node_40_1562450814267"
    },
    {
      "type": "standard",
      "title": "Concordar",
      "output": {
        "generic": []
      },
      "parent": "node_22_1562450487430",
      "metadata": {},
      "next_step": {
        "behavior": "jump_to",
        "selector": "body",
        "dialog_node": "node_38_1562450814267"
      },
      "conditions": "#concordar",
      "dialog_node": "node_23_1562450487433"
    },
    {
      "type": "standard",
      "title": "Informa foto Identidade",
      "output": {
        "generic": [
          {
            "values": [
              {
                "text": "$foto_identidade"
              }
            ],
            "response_type": "text",
            "selection_policy": "sequential"
          }
        ]
      },
      "parent": "node_10_1562444690765",
      "metadata": {},
      "dialog_node": "node_11_1562446433620"
    },
    {
      "type": "standard",
      "title": "Tentativa Foto",
      "output": {
        "generic": []
      },
      "parent": "node_13_1562447785944",
      "metadata": {},
      "next_step": {
        "behavior": "jump_to",
        "selector": "body",
        "dialog_node": "node_11_1562446433620"
      },
      "dialog_node": "node_14_1562447945154"
    },
    {
      "type": "standard",
      "title": "Tentativa Foto",
      "output": {
        "generic": []
      },
      "parent": "node_49_1562450814267",
      "metadata": {},
      "next_step": {
        "behavior": "jump_to",
        "selector": "body",
        "dialog_node": "node_40_1562450814267"
      },
      "dialog_node": "node_50_1562450814267"
    },
    {
      "type": "standard",
      "title": "Falha",
      "output": {
        "generic": [
          {
            "values": [
              {
                "text": "Poxa a foto não ficou muito boa, poderia tentar tirar outra em um local mais claro ?"
              }
            ],
            "response_type": "text",
            "selection_policy": "sequential"
          }
        ]
      },
      "parent": "node_11_1562446433620",
      "metadata": {},
      "conditions": "#discordancia",
      "dialog_node": "node_13_1562447785944",
      "previous_sibling": "node_12_1562447689636"
    },
    {
      "type": "standard",
      "title": "Sucesso",
      "output": {
        "generic": [
          {
            "values": [
              {
                "text": "Ficou ótimo, conseguimos te ver bem. Você poderia mandar uma foto do contrato da casa, contrato de aluguel ou algo do tipo ?\n"
              }
            ],
            "response_type": "text",
            "selection_policy": "sequential"
          }
        ]
      },
      "parent": "node_11_1562446433620",
      "metadata": {},
      "conditions": "#concordar",
      "dialog_node": "node_12_1562447689636"
    },
    {
      "type": "standard",
      "title": "Informa Foto Contrato",
      "output": {
        "generic": [
          {
            "values": [
              {
                "text": "$foto_contrato"
              }
            ],
            "response_type": "text",
            "selection_policy": "sequential"
          }
        ]
      },
      "parent": "node_12_1562447689636",
      "metadata": {},
      "dialog_node": "node_15_1562448230932"
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
      "previous_sibling": "node_1_1562441885816"
    },
    {
      "type": "folder",
      "title": "Noob",
      "metadata": {},
      "conditions": "$noob",
      "dialog_node": "node_1_1562441885816"
    }
  ],
  "workspace_id": "0f156808-de0f-4c7c-a97f-408808cabe79",
  "counterexamples": [],
  "system_settings": {
    "tooling": {
      "store_generic_responses": True
    }
  },
  "learning_opt_out": False,
  "status": "Available"
}