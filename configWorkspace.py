##Configurações do WATSON
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
          "text": "Claro"
        },
        {
          "text": "Sim"
        },
        {
          "text": "si"
        },
        {
          "text": "Uhum"
        },
        {
          "text": "Vamos"
        },
        {
          "text": "Com certeza"
        }
      ],
      "description": ""
    },
    {
      "intent": "informacao_alterar_titularidade",
      "examples": [
        {
          "text": "Como faço isso ?"
        },
        {
          "text": "Tenho duvidas sobre alteração de titularidade"
        },
        {
          "text": "Gostaria de mais informações sobre alterar a titularidade"
        },
        {
          "text": "Como faço para alterar a titularidade ?"
        },
        {
          "text": "Gostaria de saber mais sobre como mudar a titularidade"
        },
        {
          "text": "Como altero a titularidade ?"
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
          "text": "Trocar titularidade"
        },
        {
          "text": "Mudar titularidade"
        },
        {
          "text": "Alterar titularidade"
        },
        {
          "text": "Vou trocar a titularidade"
        },
        {
          "text": "Mudança de titularidade"
        }
      ],
      "description": "Capturar interesse em mudar a titularidade"
    },
    {
      "intent": "informacao_nova_instalacao",
      "examples": [
        {
          "text": "Tenho duvidas de como pedir uma nova instalação"
        },
        {
          "text": "Tenho duvidas de como pedir uma nova instalção"
        },
        {
          "text": "Como peço uma nova instalação ?"
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
          "text": "Olá"
        },
        {
          "text": "Oi"
        },
        {
          "text": "Opa"
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
          "text": "Estou de mudança"
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
      "intent": "foto",
      "examples": [
        {
          "text": "#foto"
        },
        {
          "text": "foto"
        }
      ],
      "description": "mensagem quando é enviada uma foto"
    },
    {
      "intent": "despedida",
      "examples": [
        {
          "text": "Isso é tudo, obrigado"
        },
        {
          "text": "Muito obrigado, tchau"
        },
        {
          "text": "Não preciso fazer mais nada, obrigado"
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
        },
        {
          "text": "Já resolvi meu problema"
        },
        {
          "text": "Tchau"
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
          "text": "Gostaria de requisitar uma nova instalação"
        },
        {
          "text": "Vou fazer uma nova instalação"
        },
        {
          "text": "Vou me mudar para uma casa nova e preciso fazer uma nova instalação"
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
      "parent": "node_73_1562459790343",
      "metadata": {},
      "dialog_node": "node_74_1562459790343"
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
      "parent": "node_44_1562450814267",
      "metadata": {},
      "conditions": "#concordar",
      "dialog_node": "node_45_1562450814267"
    },
    {
      "type": "standard",
      "title": "Tentativa Foto",
      "output": {
        "generic": []
      },
      "parent": "node_22_1562458977215",
      "metadata": {},
      "next_step": {
        "behavior": "jump_to",
        "selector": "body",
        "dialog_node": "node_14_1562458977215"
      },
      "conditions": "anything_else",
      "dialog_node": "node_23_1562458977215"
    },
    {
      "type": "standard",
      "title": "Nova tentativa foto",
      "output": {
        "generic": []
      },
      "parent": "node_76_1562459790343",
      "metadata": {},
      "next_step": {
        "behavior": "jump_to",
        "selector": "condition",
        "dialog_node": "node_72_1562459790343"
      },
      "dialog_node": "node_77_1562459790343"
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
      "parent": "node_74_1562459790343",
      "metadata": {},
      "conditions": "#concordar",
      "dialog_node": "node_75_1562459790343"
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
      "parent": "node_70_1562459790343",
      "metadata": {},
      "conditions": "#discordancia",
      "dialog_node": "node_78_1562459790343",
      "previous_sibling": "node_71_1562459790343"
    },
    {
      "type": "standard",
      "title": "Sucesso",
      "output": {
        "generic": [
          {
            "values": [
              {
                "text": "Agora você poderia mandar uma foto do contrato da casa, contrato de aluguel ou algo do tipo ?\n"
              }
            ],
            "response_type": "text",
            "selection_policy": "sequential"
          }
        ]
      },
      "parent": "node_70_1562459790343",
      "metadata": {},
      "conditions": "#concordar",
      "dialog_node": "node_71_1562459790343"
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
      "parent": "node_28_1562458977215",
      "metadata": {},
      "conditions": "anything_else",
      "dialog_node": "node_29_1562458977215"
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
      "parent": "node_58_1562459790343",
      "metadata": {},
      "conditions": "anything_else",
      "dialog_node": "node_59_1562459790343"
    },
    {
      "type": "standard",
      "title": "Tentativa Foto",
      "output": {
        "generic": []
      },
      "parent": "node_37_1562458977215",
      "metadata": {},
      "next_step": {
        "behavior": "jump_to",
        "selector": "body",
        "dialog_node": "node_29_1562458977215"
      },
      "conditions": "anything_else",
      "dialog_node": "node_38_1562458977215"
    },
    {
      "type": "standard",
      "title": "Falha",
      "output": {
        "generic": [
          {
            "values": [
              {
                "text": "A foto ficou ruim, poderia tirar outra em um local mais claro ?"
              }
            ],
            "response_type": "text",
            "selection_policy": "sequential"
          }
        ]
      },
      "parent": "node_55_1562459790343",
      "metadata": {},
      "conditions": "#discordancia",
      "dialog_node": "node_63_1562459790343",
      "previous_sibling": "node_56_1562459790343"
    },
    {
      "type": "standard",
      "title": "Sucesso",
      "output": {
        "generic": [
          {
            "values": [
              {
                "text": "Pronto! Você poderia mandar uma foto do contrato da casa, do contrato de aluguel ou algo do tipo ?\n"
              }
            ],
            "response_type": "text",
            "selection_policy": "sequential"
          }
        ]
      },
      "parent": "node_55_1562459790343",
      "metadata": {},
      "conditions": "#concordar",
      "dialog_node": "node_56_1562459790343"
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
      "title": "Nova tentativa foto",
      "output": {
        "generic": []
      },
      "parent": "node_61_1562459790343",
      "metadata": {},
      "next_step": {
        "behavior": "jump_to",
        "selector": "condition",
        "dialog_node": "node_57_1562459790343"
      },
      "conditions": "anything_else",
      "dialog_node": "node_62_1562459790343"
    },
    {
      "type": "standard",
      "title": "Informa foto Poste",
      "output": {
        "generic": [
          {
            "values": [
              {
                "text": "#foto_poste\n"
              }
            ],
            "response_type": "text",
            "selection_policy": "sequential"
          }
        ]
      },
      "parent": "node_16_1562448280556",
      "metadata": {},
      "conditions": "anything_else",
      "dialog_node": "node_19_1562450010961"
    },
    {
      "type": "standard",
      "title": "Tentativa Foto",
      "output": {
        "generic": []
      },
      "parent": "node_78_1562459790343",
      "metadata": {},
      "next_step": {
        "behavior": "jump_to",
        "selector": "body",
        "dialog_node": "node_70_1562459790343"
      },
      "conditions": "anything_else",
      "dialog_node": "node_79_1562459790343"
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
      "parent": "node_30_1562458977215",
      "metadata": {},
      "conditions": "anything_else",
      "dialog_node": "node_31_1562458977215"
    },
    {
      "type": "standard",
      "title": "Falha",
      "output": {
        "generic": [
          {
            "values": [
              {
                "text": "A foto ficou ruim, poderia tirar outra em um local mais claro ?"
              }
            ],
            "response_type": "text",
            "selection_policy": "sequential"
          }
        ]
      },
      "parent": "node_14_1562458977215",
      "metadata": {},
      "conditions": "#discordancia",
      "dialog_node": "node_22_1562458977215",
      "previous_sibling": "node_15_1562458977215"
    },
    {
      "type": "standard",
      "title": "Sucesso",
      "output": {
        "generic": [
          {
            "values": [
              {
                "text": "Pronto! Você poderia mandar uma foto do contrato da casa, do contrato de aluguel ou algo do tipo ?\n"
              }
            ],
            "response_type": "text",
            "selection_policy": "sequential"
          }
        ]
      },
      "parent": "node_14_1562458977215",
      "metadata": {},
      "conditions": "#concordar",
      "dialog_node": "node_15_1562458977215"
    },
    {
      "type": "standard",
      "title": "Mudança Duvida",
      "output": {
        "generic": [
          {
            "values": [
              {
                "text": "Para onde você vai se mudar já existe uma rede eletrica ?"
              }
            ],
            "response_type": "text",
            "selection_policy": "sequential"
          }
        ]
      },
      "parent": "node_5_1562458977190",
      "metadata": {},
      "conditions": "#fazer_mudanca",
      "dialog_node": "node_43_1562458977215",
      "previous_sibling": "node_40_1562458977215"
    },
    {
      "type": "standard",
      "title": "Requisitar nova instalação",
      "output": {
        "generic": [
          {
            "values": [
              {
                "text": "Claro. Você sabe como proceder ?"
              }
            ],
            "response_type": "text",
            "selection_policy": "sequential"
          }
        ]
      },
      "parent": "node_5_1562458977190",
      "metadata": {},
      "conditions": "#nova_instalacao",
      "dialog_node": "node_10_1562458977215",
      "previous_sibling": "node_7_1562458977213"
    },
    {
      "type": "standard",
      "title": "Requisitar nova titularidade",
      "output": {
        "generic": [
          {
            "values": [
              {
                "text": "Claro, você quer detalhes do processo ?"
              }
            ],
            "response_type": "text",
            "selection_policy": "sequential"
          }
        ]
      },
      "parent": "node_5_1562458977190",
      "metadata": {},
      "conditions": "#alterar_titularidade",
      "dialog_node": "node_25_1562458977215",
      "previous_sibling": "node_10_1562458977215"
    },
    {
      "type": "standard",
      "title": "Informação nova instalação",
      "output": {
        "generic": [
          {
            "values": [
              {
                "text": "Primeiro você precisa confirmar que não há energia no local.  Certifique-se se há um poste aderente a regulamentação na proximidade, alem disso precisamos do seu endereço, identidade e comprovante de residencia.  Você deseja começar o processo ?"
              }
            ],
            "response_type": "text",
            "selection_policy": "sequential"
          }
        ]
      },
      "parent": "node_5_1562458977190",
      "metadata": {},
      "conditions": "#informacao_nova_instalacao",
      "dialog_node": "node_7_1562458977213",
      "previous_sibling": "node_6_1562458977212"
    },
    {
      "type": "standard",
      "title": "Informação nova titularidade",
      "output": {
        "generic": [
          {
            "values": [
              {
                "text": "Precisamos da sua identidade, o endereço e algum comprovante da sua casa nova, só isso. Quer fazer isso agora ?"
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
      "parent": "node_5_1562458977190",
      "metadata": {},
      "conditions": "#informacao_alterar_titularidade",
      "dialog_node": "node_40_1562458977215",
      "previous_sibling": "node_25_1562458977215"
    },
    {
      "type": "standard",
      "title": "Bem-vindo",
      "output": {
        "generic": [
          {
            "values": [
              {
                "text": "Como posso te ajudar #nome ?"
              }
            ],
            "response_type": "text",
            "selection_policy": "random"
          }
        ]
      },
      "parent": "node_5_1562458977190",
      "metadata": {},
      "conditions": "#boas_vindas",
      "dialog_node": "node_6_1562458977212"
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
      "title": "Discordar",
      "output": {
        "generic": [
          {
            "values": [
              {
                "text": "Beleza!"
              }
            ],
            "response_type": "text",
            "selection_policy": "sequential"
          }
        ]
      },
      "parent": "node_48_1562459790343",
      "metadata": {},
      "next_step": {
        "behavior": "jump_to",
        "selector": "body",
        "dialog_node": "node_47_1562459790343"
      },
      "conditions": "#discordancia",
      "dialog_node": "node_50_1562459790343",
      "previous_sibling": "node_49_1562459790343"
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
      "parent": "node_48_1562459790343",
      "metadata": {},
      "next_step": {
        "behavior": "jump_to",
        "selector": "body",
        "dialog_node": "node_53_1562459790343"
      },
      "conditions": "#concordar",
      "dialog_node": "node_49_1562459790343"
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
      "conditions": "anything_else",
      "dialog_node": "node_10_1562444690765"
    },
    {
      "type": "standard",
      "title": "Falha",
      "output": {
        "generic": [
          {
            "values": [
              {
                "text": "A foto não ficou boa, poderia tentar tirar outra com mais luz sobre o contrato."
              }
            ],
            "response_type": "text",
            "selection_policy": "sequential"
          }
        ]
      },
      "parent": "node_57_1562459790343",
      "metadata": {},
      "conditions": "#discordancia",
      "dialog_node": "node_61_1562459790343",
      "previous_sibling": "node_58_1562459790343"
    },
    {
      "type": "standard",
      "title": "Sucesso",
      "output": {
        "generic": [
          {
            "values": [
              {
                "text": "O poste próximo precisa estar de acordo com nosso regulamento. Poderia tirar uma foto para verificarmos se ele está de acordo."
              }
            ],
            "response_type": "text",
            "selection_policy": "sequential"
          }
        ]
      },
      "parent": "node_57_1562459790343",
      "metadata": {},
      "conditions": "#concordar",
      "dialog_node": "node_58_1562459790343"
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
      "parent": "node_18_1562458977215",
      "metadata": {},
      "conditions": "#concordar",
      "dialog_node": "node_19_1562458977215"
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
      "parent": "node_43_1562458977215",
      "metadata": {},
      "next_step": {
        "behavior": "jump_to",
        "selector": "body",
        "dialog_node": "node_10_1562458977215"
      },
      "conditions": "#discordancia",
      "dialog_node": "node_45_1562458977215",
      "previous_sibling": "node_44_1562458977215"
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
      "parent": "node_43_1562458977215",
      "metadata": {},
      "next_step": {
        "behavior": "jump_to",
        "selector": "body",
        "dialog_node": "node_25_1562458977215"
      },
      "conditions": "#concordar",
      "dialog_node": "node_44_1562458977215"
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
      "parent": "node_59_1562459790343",
      "metadata": {},
      "conditions": "#concordar",
      "dialog_node": "node_60_1562459790343"
    },
    {
      "type": "standard",
      "title": "Nova tentativa foto",
      "output": {
        "generic": []
      },
      "parent": "node_35_1562458977215",
      "metadata": {},
      "next_step": {
        "behavior": "jump_to",
        "selector": "condition",
        "dialog_node": "node_31_1562458977215"
      },
      "dialog_node": "node_36_1562458977215"
    },
    {
      "type": "standard",
      "title": "Discordar",
      "output": {
        "generic": [
          {
            "values": [
              {
                "text": "Beleza!"
              }
            ],
            "response_type": "text",
            "selection_policy": "sequential"
          }
        ]
      },
      "parent": "node_40_1562458977215",
      "metadata": {},
      "next_step": {
        "behavior": "jump_to",
        "selector": "body",
        "dialog_node": "node_6_1562458977212"
      },
      "conditions": "#discordancia",
      "dialog_node": "node_42_1562458977215",
      "previous_sibling": "node_41_1562458977215"
    },
    {
      "type": "standard",
      "title": "Concordar",
      "output": {
        "generic": []
      },
      "parent": "node_40_1562458977215",
      "metadata": {},
      "next_step": {
        "behavior": "jump_to",
        "selector": "body",
        "dialog_node": "node_27_1562458977215"
      },
      "conditions": "#concordar",
      "dialog_node": "node_41_1562458977215"
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
      "conditions": "anything_else",
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
      "conditions": "anything_else",
      "dialog_node": "node_18_1562449817771"
    },
    {
      "type": "standard",
      "title": "Discordar",
      "output": {
        "generic": [
          {
            "values": [
              {
                "text": "Beleza!"
              }
            ],
            "response_type": "text",
            "selection_policy": "sequential"
          }
        ]
      },
      "parent": "node_7_1562458977213",
      "metadata": {},
      "next_step": {
        "behavior": "jump_to",
        "selector": "body",
        "dialog_node": "node_6_1562458977212"
      },
      "conditions": "#discordancia",
      "dialog_node": "node_9_1562458977214",
      "previous_sibling": "node_8_1562458977213"
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
      "parent": "node_7_1562458977213",
      "metadata": {},
      "next_step": {
        "behavior": "jump_to",
        "selector": "body",
        "dialog_node": "node_12_1562458977215"
      },
      "conditions": "#concordar",
      "dialog_node": "node_8_1562458977213"
    },
    {
      "type": "standard",
      "title": "Não entendi",
      "output": {
        "generic": [
          {
            "values": [
              {
                "text": "Desculpe não entendi, estavamos falando de uma nova instalação. "
              }
            ],
            "response_type": "text",
            "selection_policy": "sequential"
          }
        ]
      },
      "parent": "node_10_1562458977215",
      "metadata": {},
      "conditions": "anything_else",
      "dialog_node": "node_24_1562458977215",
      "previous_sibling": "node_12_1562458977215"
    },
    {
      "type": "standard",
      "title": "Discordar da ajuda",
      "output": {
        "generic": [
          {
            "values": [
              {
                "text": "Qual o endereço da nova instalação ?"
              }
            ],
            "response_type": "text",
            "selection_policy": "sequential"
          }
        ]
      },
      "parent": "node_10_1562458977215",
      "metadata": {},
      "conditions": "#discordancia",
      "dialog_node": "node_12_1562458977215",
      "previous_sibling": "node_11_1562458977215"
    },
    {
      "type": "standard",
      "title": "Concordar com ajuda",
      "output": {
        "generic": []
      },
      "parent": "node_10_1562458977215",
      "metadata": {},
      "next_step": {
        "behavior": "jump_to",
        "selector": "body",
        "dialog_node": "node_7_1562458977213"
      },
      "conditions": "#concordar",
      "dialog_node": "node_11_1562458977215"
    },
    {
      "type": "standard",
      "title": "Falha",
      "output": {
        "generic": [
          {
            "values": [
              {
                "text": "A foto não ficou boa, poderia tentar tirar outra com mais luz sobre o contrato."
              }
            ],
            "response_type": "text",
            "selection_policy": "sequential"
          }
        ]
      },
      "parent": "node_16_1562458977215",
      "metadata": {},
      "conditions": "#discordancia",
      "dialog_node": "node_20_1562458977215",
      "previous_sibling": "node_17_1562458977215"
    },
    {
      "type": "standard",
      "title": "Sucesso",
      "output": {
        "generic": [
          {
            "values": [
              {
                "text": "O poste próximo precisa estar de acordo com nosso regulamento. Poderia tirar uma foto para verificarmos se ele está de acordo."
              }
            ],
            "response_type": "text",
            "selection_policy": "sequential"
          }
        ]
      },
      "parent": "node_16_1562458977215",
      "metadata": {},
      "conditions": "#concordar",
      "dialog_node": "node_17_1562458977215"
    },
    {
      "type": "standard",
      "title": "Não entendi",
      "output": {
        "generic": [
          {
            "values": [
              {
                "text": "Desculpe não entendi, estavamos falando de uma nova instalação. "
              }
            ],
            "response_type": "text",
            "selection_policy": "sequential"
          }
        ]
      },
      "parent": "node_5_1562443608008",
      "metadata": {},
      "conditions": "anything_else",
      "dialog_node": "node_2_1562458593469",
      "previous_sibling": "node_8_1562444129830"
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
      "parent": "node_13_1562458977215",
      "metadata": {},
      "conditions": "anything_else",
      "dialog_node": "node_14_1562458977215"
    },
    {
      "type": "standard",
      "title": "Informa Endereço",
      "output": {
        "generic": [
          {
            "values": [
              {
                "text": "Preciso só que me confirme sua identidade. Poderia me mandar uma foto sua segurando seu RG (com a foto pra camera) ?\n"
              }
            ],
            "response_type": "text",
            "selection_policy": "sequential"
          }
        ]
      },
      "parent": "node_12_1562458977215",
      "metadata": {},
      "conditions": "anything_else",
      "dialog_node": "node_13_1562458977215"
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
      "parent": "node_29_1562458977215",
      "metadata": {},
      "conditions": "#discordancia",
      "dialog_node": "node_37_1562458977215",
      "previous_sibling": "node_30_1562458977215"
    },
    {
      "type": "standard",
      "title": "Sucesso",
      "output": {
        "generic": [
          {
            "values": [
              {
                "text": "Agora você poderia mandar uma foto do contrato da casa, contrato de aluguel ou algo do tipo ?\n"
              }
            ],
            "response_type": "text",
            "selection_policy": "sequential"
          }
        ]
      },
      "parent": "node_29_1562458977215",
      "metadata": {},
      "conditions": "#concordar",
      "dialog_node": "node_30_1562458977215"
    },
    {
      "type": "standard",
      "title": "Discordar da ajuda",
      "output": {
        "generic": [
          {
            "values": [
              {
                "text": "Qual é o endereço da nova titularidade ?"
              }
            ],
            "response_type": "text",
            "selection_policy": "sequential"
          }
        ]
      },
      "parent": "node_66_1562459790343",
      "metadata": {},
      "conditions": "#discordancia",
      "dialog_node": "node_68_1562459790343",
      "previous_sibling": "node_67_1562459790343"
    },
    {
      "type": "standard",
      "title": "Não entendi",
      "output": {
        "generic": [
          {
            "values": [
              {
                "text": "Desculpe não entendi, estavamos falando de uma mudar uma titularidade. "
              }
            ],
            "response_type": "text",
            "selection_policy": "sequential"
          }
        ]
      },
      "parent": "node_66_1562459790343",
      "metadata": {},
      "conditions": "anything_else",
      "dialog_node": "node_80_1562459790343",
      "previous_sibling": "node_68_1562459790343"
    },
    {
      "type": "standard",
      "title": "Concordar da ajuda",
      "output": {
        "generic": []
      },
      "parent": "node_66_1562459790343",
      "metadata": {},
      "next_step": {
        "behavior": "jump_to",
        "selector": "body",
        "dialog_node": "node_81_1562459790343"
      },
      "conditions": "#concordar",
      "dialog_node": "node_67_1562459790343"
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
      "title": "Não entendi",
      "output": {
        "generic": [
          {
            "values": [
              {
                "text": "Desculpe não entendi, estavamos falando de uma mudar uma titularidade. "
              }
            ],
            "response_type": "text",
            "selection_policy": "sequential"
          }
        ]
      },
      "parent": "node_36_1562450814265",
      "metadata": {},
      "conditions": "anything_else",
      "dialog_node": "node_3_1562458743353",
      "previous_sibling": "node_38_1562450814267"
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
      "title": "Discordar",
      "output": {
        "generic": [
          {
            "values": [
              {
                "text": "Beleza!"
              }
            ],
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
        "dialog_node": "Bem-vindo"
      },
      "conditions": "#discordancia",
      "dialog_node": "node_1_1562458528136",
      "previous_sibling": "node_9_1562444357961"
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
      "title": "Informa Endereço",
      "output": {
        "generic": [
          {
            "values": [
              {
                "text": "Preciso só que me confirme sua identidade. Você poderia me mandar uma foto sua segurando seu RG (com a foto pra camera) ?\n"
              }
            ],
            "response_type": "text",
            "selection_policy": "sequential"
          }
        ]
      },
      "parent": "node_53_1562459790343",
      "metadata": {},
      "conditions": "anything_else",
      "dialog_node": "node_54_1562459790343"
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
      "parent": "node_72_1562459790343",
      "metadata": {},
      "conditions": "#discordancia",
      "dialog_node": "node_76_1562459790343",
      "previous_sibling": "node_73_1562459790343"
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
      "parent": "node_72_1562459790343",
      "metadata": {},
      "conditions": "#concordar",
      "dialog_node": "node_73_1562459790343"
    },
    {
      "type": "standard",
      "title": "Informa Foto Contrato",
      "output": {
        "generic": [
          {
            "values": [
              {
                "text": "#foto_contrato"
              }
            ],
            "response_type": "text",
            "selection_policy": "sequential"
          }
        ]
      },
      "parent": "node_41_1562450814267",
      "metadata": {},
      "conditions": "anything_else",
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
      "parent": "node_17_1562458977215",
      "metadata": {},
      "conditions": "anything_else",
      "dialog_node": "node_18_1562458977215"
    },
    {
      "type": "standard",
      "title": "Tentativa Foto",
      "output": {
        "generic": []
      },
      "parent": "node_63_1562459790343",
      "metadata": {},
      "next_step": {
        "behavior": "jump_to",
        "selector": "body",
        "dialog_node": "node_55_1562459790343"
      },
      "conditions": "anything_else",
      "dialog_node": "node_64_1562459790343"
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
      "parent": "node_15_1562458977215",
      "metadata": {},
      "conditions": "anything_else",
      "dialog_node": "node_16_1562458977215"
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
      "parent": "node_71_1562459790343",
      "metadata": {},
      "conditions": "anything_else",
      "dialog_node": "node_72_1562459790343"
    },
    {
      "type": "standard",
      "title": "Informa Endereço",
      "output": {
        "generic": [
          {
            "values": [
              {
                "text": "Agora preciso só que me confirme sua identidade. Pode me mandar uma foto sua segurando seu RG (com a foto pra camera) ?\n"
              }
            ],
            "response_type": "text",
            "selection_policy": "sequential"
          }
        ]
      },
      "parent": "node_68_1562459790343",
      "metadata": {},
      "conditions": "anything_else",
      "dialog_node": "node_69_1562459790343"
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
      "parent": "node_84_1562459790343",
      "metadata": {},
      "next_step": {
        "behavior": "jump_to",
        "selector": "body",
        "dialog_node": "node_51_1562459790343"
      },
      "conditions": "#discordancia",
      "dialog_node": "node_86_1562459790343",
      "previous_sibling": "node_85_1562459790343"
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
      "parent": "node_84_1562459790343",
      "metadata": {},
      "next_step": {
        "behavior": "jump_to",
        "selector": "body",
        "dialog_node": "node_66_1562459790343"
      },
      "conditions": "#concordar",
      "dialog_node": "node_85_1562459790343"
    },
    {
      "type": "standard",
      "title": "Discordar",
      "output": {
        "generic": [
          {
            "values": [
              {
                "text": "Beleza!"
              }
            ],
            "response_type": "text",
            "selection_policy": "sequential"
          }
        ]
      },
      "parent": "node_81_1562459790343",
      "metadata": {},
      "next_step": {
        "behavior": "jump_to",
        "selector": "body",
        "dialog_node": "node_47_1562459790343"
      },
      "conditions": "#discordancia",
      "dialog_node": "node_83_1562459790343",
      "previous_sibling": "node_82_1562459790343"
    },
    {
      "type": "standard",
      "title": "Concordar",
      "output": {
        "generic": []
      },
      "parent": "node_81_1562459790343",
      "metadata": {},
      "next_step": {
        "behavior": "jump_to",
        "selector": "body",
        "dialog_node": "node_68_1562459790343"
      },
      "conditions": "#concordar",
      "dialog_node": "node_82_1562459790343"
    },
    {
      "type": "standard",
      "title": "Nova tentativa foto",
      "output": {
        "generic": []
      },
      "parent": "node_20_1562458977215",
      "metadata": {},
      "next_step": {
        "behavior": "jump_to",
        "selector": "condition",
        "dialog_node": "node_16_1562458977215"
      },
      "conditions": "anything_else",
      "dialog_node": "node_21_1562458977215"
    },
    {
      "type": "standard",
      "title": "Informa foto Poste",
      "output": {
        "generic": [
          {
            "values": [
              {
                "text": "#foto_poste\n"
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
                "text": "Vou te explicar como funciona. Primeiro você precisa confirmar que realmente não há energia no local.  Se realmente não houver, por favor certifique-se se há um posto aderente a regulamentação na proximidade. Depois disso precisaremos do endereço, da sua identidade e um comprovante de moradia.  Pronto para começar o processo ?"
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
                "text": "Tudo certo #nome ? Como posso te ajudar?"
              },
              {
                "text": "Fala #nome ? Como posso te ajudar ?"
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
      "parent": "node_32_1562458977215",
      "metadata": {},
      "dialog_node": "node_33_1562458977215"
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
      "parent": "node_54_1562459790343",
      "metadata": {},
      "conditions": "anything_else",
      "dialog_node": "node_55_1562459790343"
    },
    {
      "type": "standard",
      "title": "Discordar da ajuda",
      "output": {
        "generic": [
          {
            "values": [
              {
                "text": "Qual é o endereço da nova titularidade ?"
              }
            ],
            "response_type": "text",
            "selection_policy": "sequential"
          }
        ]
      },
      "parent": "node_25_1562458977215",
      "metadata": {},
      "conditions": "#discordancia",
      "dialog_node": "node_27_1562458977215",
      "previous_sibling": "node_26_1562458977215"
    },
    {
      "type": "standard",
      "title": "Não entendi",
      "output": {
        "generic": [
          {
            "values": [
              {
                "text": "Desculpe não entendi, estavamos falando de uma mudar uma titularidade. "
              }
            ],
            "response_type": "text",
            "selection_policy": "sequential"
          }
        ]
      },
      "parent": "node_25_1562458977215",
      "metadata": {},
      "conditions": "anything_else",
      "dialog_node": "node_39_1562458977215",
      "previous_sibling": "node_27_1562458977215"
    },
    {
      "type": "standard",
      "title": "Concordar da ajuda",
      "output": {
        "generic": []
      },
      "parent": "node_25_1562458977215",
      "metadata": {},
      "next_step": {
        "behavior": "jump_to",
        "selector": "body",
        "dialog_node": "node_40_1562458977215"
      },
      "conditions": "#concordar",
      "dialog_node": "node_26_1562458977215"
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
      "title": "Recusa a mandar foto",
      "output": {
        "generic": [
          {
            "values": [
              {
                "text": "Recusa de Foto"
              }
            ],
            "response_type": "text",
            "selection_policy": "sequential"
          }
        ]
      },
      "parent": "node_39_1562450814267",
      "metadata": {},
      "conditions": "anything_else",
      "dialog_node": "node_87_1562476241182",
      "previous_sibling": "node_40_1562450814267"
    },
    {
      "type": "standard",
      "title": "Informa foto Identidade",
      "output": {
        "generic": [
          {
            "values": [
              {
                "text": "foto_identidade"
              }
            ],
            "response_type": "text",
            "selection_policy": "random"
          }
        ]
      },
      "parent": "node_39_1562450814267",
      "metadata": {},
      "conditions": "#foto",
      "dialog_node": "node_40_1562450814267"
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
      "parent": "node_69_1562459790343",
      "metadata": {},
      "conditions": "anything_else",
      "dialog_node": "node_70_1562459790343"
    },
    {
      "type": "standard",
      "title": "Informa Endereço",
      "output": {
        "generic": [
          {
            "values": [
              {
                "text": "Agora preciso só que me confirme sua identidade. Pode me mandar uma foto sua segurando seu RG (com a foto pra camera) ?\n"
              }
            ],
            "response_type": "text",
            "selection_policy": "sequential"
          }
        ]
      },
      "parent": "node_27_1562458977215",
      "metadata": {},
      "conditions": "anything_else",
      "dialog_node": "node_28_1562458977215"
    },
    {
      "type": "standard",
      "title": "Discordar",
      "output": {
        "generic": [
          {
            "values": [
              {
                "text": "Beleza!"
              }
            ],
            "response_type": "text",
            "selection_policy": "sequential"
          }
        ]
      },
      "parent": "node_22_1562450487430",
      "metadata": {},
      "next_step": {
        "behavior": "jump_to",
        "selector": "body",
        "dialog_node": "Bem-vindo"
      },
      "conditions": "#discordancia",
      "dialog_node": "node_4_1562458783208",
      "previous_sibling": "node_23_1562450487433"
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
                "text": "foto_teste"
              }
            ],
            "response_type": "text",
            "selection_policy": "sequential"
          }
        ]
      },
      "parent": "node_10_1562444690765",
      "metadata": {},
      "conditions": "anything_else",
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
      "conditions": "anything_else",
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
      "conditions": "anything_else",
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
      "parent": "node_56_1562459790343",
      "metadata": {},
      "conditions": "anything_else",
      "dialog_node": "node_57_1562459790343"
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
      "parent": "node_31_1562458977215",
      "metadata": {},
      "conditions": "#discordancia",
      "dialog_node": "node_35_1562458977215",
      "previous_sibling": "node_32_1562458977215"
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
      "parent": "node_31_1562458977215",
      "metadata": {},
      "conditions": "#concordar",
      "dialog_node": "node_32_1562458977215"
    },
    {
      "type": "standard",
      "title": "Não entendi",
      "output": {
        "generic": [
          {
            "values": [
              {
                "text": "Desculpe não entendi, estavamos falando de uma nova instalação. "
              }
            ],
            "response_type": "text",
            "selection_policy": "sequential"
          }
        ]
      },
      "parent": "node_51_1562459790343",
      "metadata": {},
      "conditions": "anything_else",
      "dialog_node": "node_65_1562459790343",
      "previous_sibling": "node_53_1562459790343"
    },
    {
      "type": "standard",
      "title": "Discordar da ajuda",
      "output": {
        "generic": [
          {
            "values": [
              {
                "text": "Vou lhe pedir alguns dados, mas não se preocupe eles estarão seguros. Qual o endereço da nova instalação ? "
              }
            ],
            "response_type": "text",
            "selection_policy": "sequential"
          }
        ]
      },
      "parent": "node_51_1562459790343",
      "metadata": {},
      "conditions": "#discordancia",
      "dialog_node": "node_53_1562459790343",
      "previous_sibling": "node_52_1562459790343"
    },
    {
      "type": "standard",
      "title": "Concordar com ajuda",
      "output": {
        "generic": []
      },
      "parent": "node_51_1562459790343",
      "metadata": {},
      "next_step": {
        "behavior": "jump_to",
        "selector": "body",
        "dialog_node": "node_48_1562459790343"
      },
      "conditions": "#concordar",
      "dialog_node": "node_52_1562459790343"
    },
    {
      "type": "standard",
      "title": "Requisitar nova instalação",
      "output": {
        "generic": [
          {
            "values": [
              {
                "text": "Claro. Você sabe como proceder ?"
              }
            ],
            "response_type": "text",
            "selection_policy": "sequential"
          }
        ]
      },
      "parent": "node_46_1562459790323",
      "metadata": {},
      "conditions": "#nova_instalacao",
      "dialog_node": "node_51_1562459790343",
      "previous_sibling": "node_48_1562459790343"
    },
    {
      "type": "standard",
      "title": "Informação nova titularidade",
      "output": {
        "generic": [
          {
            "values": [
              {
                "text": "Precisamos da sua identidade, o endereço e algum comprovante da sua casa nova, mas fica tranquilo que seus dados estarão seguros e não serão compartilhados. Quer fazer isso agora ?"
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
      "parent": "node_46_1562459790323",
      "metadata": {},
      "conditions": "#informacao_alterar_titularidade",
      "dialog_node": "node_81_1562459790343",
      "previous_sibling": "node_66_1562459790343"
    },
    {
      "type": "standard",
      "title": "Mudança Duvida",
      "output": {
        "generic": [
          {
            "values": [
              {
                "text": "Lá já possui uma instalação elétrica atualmente ?"
              }
            ],
            "response_type": "text",
            "selection_policy": "sequential"
          }
        ]
      },
      "parent": "node_46_1562459790323",
      "metadata": {},
      "conditions": "#fazer_mudanca",
      "dialog_node": "node_84_1562459790343",
      "previous_sibling": "node_81_1562459790343"
    },
    {
      "type": "standard",
      "title": "Informação nova instalação",
      "output": {
        "generic": [
          {
            "values": [
              {
                "text": "Primeiro você precisa confirmar que não há energia no local.  Certifique-se se há um poste aderente a regulamentação na proximidade. Alem disso precisaremos de confirmar sua identidade, um endereço e um comprovante de residencia, mas fica tranquilo que seus dados estarão seguros e não serão compartilhados.  Você deseja começar o processo ?"
              }
            ],
            "response_type": "text",
            "selection_policy": "sequential"
          }
        ]
      },
      "parent": "node_46_1562459790323",
      "metadata": {},
      "conditions": "#informacao_nova_instalacao",
      "dialog_node": "node_48_1562459790343",
      "previous_sibling": "node_47_1562459790343"
    },
    {
      "type": "standard",
      "title": "Requisitar nova titularidade",
      "output": {
        "generic": [
          {
            "values": [
              {
                "text": "Claro, você quer detalhes do processo ?"
              }
            ],
            "response_type": "text",
            "selection_policy": "sequential"
          }
        ]
      },
      "parent": "node_46_1562459790323",
      "metadata": {},
      "conditions": "#alterar_titularidade",
      "dialog_node": "node_66_1562459790343",
      "previous_sibling": "node_51_1562459790343"
    },
    {
      "type": "standard",
      "title": "Bem-vindo",
      "output": {
        "generic": [
          {
            "values": [
              {
                "text": "Olá #nome, sou seu assistente, como posso te ajudar?"
              }
            ],
            "response_type": "text",
            "selection_policy": "random"
          }
        ]
      },
      "parent": "node_46_1562459790323",
      "metadata": {},
      "conditions": "#boas_vindas",
      "dialog_node": "node_47_1562459790343"
    },
    {
      "type": "standard",
      "title": "Informa Foto Contrato",
      "output": {
        "generic": [
          {
            "values": [
              {
                "text": "#foto_contrato"
              }
            ],
            "response_type": "text",
            "selection_policy": "sequential"
          }
        ]
      },
      "parent": "node_12_1562447689636",
      "metadata": {},
      "conditions": "anything_else",
      "dialog_node": "node_15_1562448230932"
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
      "parent": "node_33_1562458977215",
      "metadata": {},
      "conditions": "#concordar",
      "dialog_node": "node_34_1562458977215"
    },
    {
      "type": "folder",
      "title": "Conservador",
      "metadata": {},
      "conditions": "$conservador",
      "dialog_node": "node_46_1562459790323",
      "previous_sibling": "node_5_1562458977190"
    },
    {
      "type": "folder",
      "title": "Sem Tempo",
      "metadata": {},
      "conditions": "$semtempo",
      "dialog_node": "node_5_1562458977190",
      "previous_sibling": "node_1_1562441885816"
    },
    {
      "type": "standard",
      "title": "Em outros casos",
      "output": {
        "generic": [
          {
            "values": [
              {
                "text": "Eu não entendi. Como posso te ajudar ?"
              },
              {
                "text": "Você pode reformular? Não entendi muito bem como posso lhe ajudar"
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
      "previous_sibling": "node_46_1562459790323"
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
  "counterexamples": [
    {
      "text": "Casa"
    }
  ],
  "system_settings": {
    "tooling": {
      "store_generic_responses": True
    }
  },
  "learning_opt_out": False,
  "status": "Available"
}